from pagniation_code import PaginationHelper
import unittest

class Test_PaginationHelper(unittest.TestCase):

    def test_inputs(self):
        collection = range(1,25)
        test = PaginationHelper(collection,10)
        self.assertEqual(test.page_count(), 3, 'page_count is returning incorrect value.')
        self.assertEqual(test.page_index(23), 2, 'page_index returned incorrect value')
        self.assertEqual(test.page_item_count(2), 4, 'page_item_count returned incorrect value')
        self.assertEqual(test.item_count(), 24, 'item_count returned incorrect value')

    def test_negative_inputs(self):
        collection = range(1,25)
        test = PaginationHelper(collection,10)
        self.assertEqual(test.page_index(-1), -1, 'page_index returned incorrect value')
        self.assertEqual(test.page_item_count(-1), -1, 'page_item_count returned incorrect value')

    def test_outofrange_inputs(self):
        collection = range(1,25)
        test = PaginationHelper(collection,10)
        self.assertEqual(test.page_index(30), -1, 'page_index returned incorrect value')
        self.assertEqual(test.page_item_count(5), -1, 'page_item_count returned incorrect value')

unittest.main()