class Library:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def delete_book(self, book):
        self.book_list.remove(book)

    def delete_book_index(self, index):
        self.book_list.pop(index)

    def add_book(self, book):
        self.book_list.append(book)

    def check_out_book(self, book):
        book.checked_out = True

    def check_book_in(self, book):
        book.checked_out = False