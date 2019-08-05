"""Used to maintain a Google Sheet with basic columns of ID, Room, Item, and Cost."""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
worksheet = client.open("Py House Inventory").sheet1


def get_id_list():
    items = get_items()
    id_list = [item['ID'] for item in items]
    return id_list


def get_items():
    list_of_hashes = worksheet.get_all_records()
    return list_of_hashes


def get_row_number(item_id):
    id_list = get_id_list()
    row = id_list.index(item_id) + 2
    return row


def delete_item(item_id):
    row = get_row_number(item_id)
    response = worksheet.delete_row(row)
    return not bool(response['replies'][0])


def insert_item(new_item):
    id_list = get_id_list()
    row_index = len(id_list) + 2  # Add two to get next row and leave space for header

    # Get the next ID number and prepend it to new_item
    next_id = max(id_list)+1
    new_item.insert(0, next_id)

    worksheet.insert_row(new_item, row_index)
    return new_item


def update_item(updated_item):
    row = str(get_row_number(updated_item[0]))

    # Construct a list of cells to update
    cell_list = worksheet.range('A' + row + ':D' + row)
    for cell, value in zip(cell_list, updated_item):
        cell.value = value

    response = worksheet.update_cells(cell_list)
    return response['updatedRows'] == 1


if __name__ == '__main__':
    # Testing
    # insert_item(['Test', 'testthis', 0])
    # update_item([10, 'New!!', 'Updated this!', 50])
    # print(delete_item(6))
    pass
