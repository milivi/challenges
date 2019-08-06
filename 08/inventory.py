"""Used to maintain a Google Sheet with basic columns of ID, Room, Item, and Cost."""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class InventoryManager:
    def __init__(self):
        # Use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        self.spreadsheet = client.open("Py House Inventory")
        self.worksheet = self.spreadsheet.sheet1

    def get_id_list(self):
        items = self.get_items()
        id_list = [item['ID'] for item in items]
        return id_list

    def get_items(self):
        list_of_hashes = self.worksheet.get_all_records()
        return list_of_hashes

    def get_row_number(self, item_id):
        id_list = self.get_id_list()
        # Handle when the item_id does not exist
        try:
            row = id_list.index(item_id) + 2
        except ValueError:
            row = None
        return row

    def delete_item(self, item_id):
        row = self.get_row_number(item_id)
        if row:
            response = self.worksheet.delete_row(row)
            response = not bool(response['replies'][0])
        else:
            response = False
        return response

    def insert_item(self, new_item):
        id_list = self.get_id_list()
        row_index = len(id_list) + 2  # Add two to get next row and leave space for header

        # Get the next ID number and prepend it to new_item
        next_id = max(id_list)+1 if id_list else 1  # Handle an empty list
        new_item.insert(0, next_id)

        response = self.worksheet.insert_row(new_item, row_index)
        return response['updatedRows'] == 1

    def update_item(self, updated_item):
        row = self.get_row_number(updated_item[0])
        if row:
            row = str(row)
            # Construct a list of cells to update
            cell_list = self.worksheet.range('A' + row + ':D' + row)
            for cell, value in zip(cell_list, updated_item):
                cell.value = value

            response = self.worksheet.update_cells(cell_list)
        else:
            response = {'updatedRows': 0}
        return response['updatedRows'] == 1
