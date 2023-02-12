import unittest
from models.library import *
from models.book import *

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("Test Library")
        self.book_1 = Book("The Shining", "Stephen King", "Horror")
        self.book_2 = Book("Under the Skin", "Michael Faber", "Science Fiction")
        self.book_3 = Book("Moneyland", "Oliver Bullough", "Non-Fiction")
        self.book_4 = Book("Birdsong", "Sebastian Faulks", "War")
        self.book_5 = Book("The Bone Clocks", "David Mitchell", "Science Fiction")

# Testing Library has a name
    def test_library_has_a_name(self):
        self.assertEqual("Test Library", self.library.name)

# Testing book can be added to the book_list 
    def test_book_can_be_added_to_list(self):
        self.library.add_book(self.book_1)
        self.assertEqual(1, len(self.library.book_list))

    def test_multiple_books_can_be_added_to_library(self):
        self.library.add_book(self.book_1)
        self.library.add_book(self.book_2)
        self.library.add_book(self.book_3)
        self.library.add_book(self.book_4)
        self.library.add_book(self.book_5)
        self.assertEqual(5, len(self.library.book_list))
        self.assertEqual(self.book_5, self.library.book_list[-1])
        self.assertEqual(self.book_1, self.library.book_list[0])

# Testing book check_out status can be changed
    def test_book_can_be_checked_out__True(self):
        self.library.check_out_book(self.book_1)
        self.assertEqual(True, self.book_1.checked_out) 
  
    def test_book_can_be_checked_out__False(self):
        self.library.check_book_in(self.book_1)
        self.assertEqual(False, self.book_1.checked_out)

# Testing a book can be deleted from the book_list
    def test_book_can_be_deleted(self):
        self.library.book_list = [self.book_1, self.book_2, self.book_3]
        self.library.delete_book(self.book_1)
        self.assertEqual(2, len(self.library.book_list))
        
    def test_book_can_be_deleted_by_index(self):
        self.library.book_list = [self.book_1, self.book_2, self.book_3]
        self.library.delete_book_index(0)
        self.assertEqual(2, len(self.library.book_list))