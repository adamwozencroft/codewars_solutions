class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.array = collection
        self.array_len = len(self.array)
        self.page_lim = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return self.array_len

    # returns the number of pages
    def page_count(self):
        return (self.array_len//self.page_lim)+1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index+1 > self.page_count() or page_index < 0:
            return -1
        elif page_index == self.page_count()-1:
            items_on_page = self.array[self.page_lim*page_index:]
            return len(items_on_page)
        else:
            return self.page_lim

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index+1 > self.array_len or item_index < 0:
            return -1
        else:
            return int(item_index/self.page_lim)