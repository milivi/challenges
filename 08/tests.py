"""Tests for the inventory functions."""

import unittest

from inventory import InventoryManager


class TestInventory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.my_manager = InventoryManager()
        cls.my_manager.worksheet = cls.my_manager.spreadsheet.add_worksheet('test', 25, 4)
        cls.my_manager.worksheet.insert_row(['ID', 'Room', 'Item', 'Cost'])

    def test_happy(self):
        # test_insert_item
        self.assertTrue(
            self.my_manager.insert_item(
                ['Basement',
                 'Futon',
                 600]
            ),
            msg='Insert Failed')

        # test_get_items(self):
        self.assertEqual(self.my_manager.get_items(),
                         [{'ID': 1,
                           'Room': 'Basement',
                           'Item': 'Futon',
                           'Cost': 600}],
                         msg='Could not get inserted item.')

        # test_get_id_list
        self.assertEqual(self.my_manager.get_id_list(),
                         [1],
                         msg='ID List incorrect')

        # test_get_row_number
        self.assertEqual(self.my_manager.get_row_number(1),
                         2,
                         msg='Row Number Incorrect')

        # test_update
        update = [
            1,
            'Family Room',
            'Futon',
            600
        ]
        self.assertTrue(self.my_manager.update_item(update), msg='Item Update Failed')

        self.assertEqual(self.my_manager.get_items(),
                         [{'ID': 1,
                           'Room': 'Family Room',
                           'Item': 'Futon',
                           'Cost': 600}],
                         msg='Item Not Actually Updated')

        # test_delete(self):
        self.assertTrue(self.my_manager.delete_item(1), msg='Could not delete')

        self.assertEqual(self.my_manager.get_id_list(),
                         [],
                         msg='Did not delete item')

        # test deleting something that is not there
        self.assertFalse(self.my_manager.delete_item(1), msg='Should have indicated unable to delete')

        # test updating something that is not there
        self.assertFalse(self.my_manager.update_item(update), msg='Should have indicated unable to update')

    @classmethod
    def tearDownClass(cls):
        cls.my_manager.spreadsheet.del_worksheet(cls.my_manager.worksheet)


if __name__ == '__main__':
    unittest.main()
