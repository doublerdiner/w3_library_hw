from models.book import Book
from models.library import *

book_1 = Book("The Shining", "Stephen King", "Horror")
book_2 = Book("Under the Skin", "Michael Faber", "Science Fiction")
book_3 = Book("Moneyland", "Oliver Bullough", "Non-Fiction")
book_4 = Book("Birdsong", "Sebastian Faulks", "War")
book_5 = Book("The Bone Clocks", "David Mitchell", "Science Fiction")

library = Library("CodeClan Library")

library.book_list = [book_1, book_2, book_3, book_4, book_5]

