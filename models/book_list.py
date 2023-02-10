from models.book import Book

book_1 = Book("The Shining", "Stephen King", "Horror")
book_2 = Book("Under the Skin", "Michael Faber", "Science Fiction")
book_3 = Book("Moneyland", "Oliver Bullough", "Non-Fiction")
book_4 = Book("Birdsong", "Sebastian Faulks", "War")
book_5 = Book("The Bone Clocks", "David Mitchell", "Science Fiction")

book_list = [book_1, book_2, book_3, book_4, book_5]

def delete_book(title, list=book_list):
    for book in list:
        if title == book.title:
            list.remove(book)

def delete_book_index(index, list=book_list):
    list.pop(index)

def add_book(book, list=book_list):
    list.append(book)

def check_out_book(book):
    book.checked_out = True

def check_book_in(book):
    book.checked_out = False