import unittest
from models.book import *

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


