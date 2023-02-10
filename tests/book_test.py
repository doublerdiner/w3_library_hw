import unittest
from models.book import Book
from models.book_list import *

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("The Shining", "Stephen King", "Horror")
        
# Testing that the Book class has a title, author, genre and check-out status
    def test_book_has_title(self):
        self.assertEqual("The Shining", self.book_1.title)
    
    def test_book_has_author(self):
        self.assertEqual("Stephen King", self.book_1.author)

    def test_book_has_genre(self):
        self.assertEqual("Horror", self.book_1.genre)

    def test_book_has_a_check_out_status(self):
        self.assertEqual(False, self.book_1.checked_out)

# Testing a book can be deleted from the book_list
    def test_book_can_be_deleted(self):
        book_list = [book_1, book_2, book_3, book_4, book_5]
        delete_book("The Shining", book_list)
        self.assertEqual(4, len(book_list))
        
    def test_book_can_be_deleted_by_index(self):
        book_list = [book_1, book_2, book_3, book_4, book_5]
        delete_book_index(0, book_list)
        self.assertEqual(4, len(book_list))

# Testing book can be added to the book_list 
    def test_book_can_be_added_to_list(self):
        book_list = [book_3, book_4, book_5]
        add_book(book_1, book_list)
        self.assertEqual(4, len(book_list))
        self.assertEqual(book_list[-1], book_1)

# Testing book check_out status can be changed
    def test_book_can_be_checked_out__True(self):
        check_out_book(book_1)
        self.assertEqual(True, book_1.checked_out)

    def test_book_can_be_checked_out__False(self):
        check_book_in(book_1)
        self.assertEqual(False, book_1.checked_out)
