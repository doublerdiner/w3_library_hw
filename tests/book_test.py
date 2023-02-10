import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("The Shining", "Steven King", "Horror")

    def test_book_has_title(self):
        self.assertEqual("The Shining", self.book_1.title)