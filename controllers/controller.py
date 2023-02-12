from flask import render_template, request, redirect
from app import app
from models.book_list import *
from models.book import Book
from models.library import Library
import datetime

@app.route("/library")
def index():
    return render_template("index.html", title="Home", book_list=library.book_list)

@app.route("/library/<index>")
def book_view(index):
    index = int(index)
    book_to_view = library.book_list[index]
    return render_template("book.html", title="Book", book=book_to_view, index=index)

@app.route("/library/<index>", methods=['POST'])
def post_update_check_status(index):
    index = int(index)
    book_to_check_out = library.book_list[index]
    if request.form["status"] == "CheckIn":
        library.check_book_in(book_to_check_out)
        book_to_check_out.due_date = None
    else:
        library.check_out_book(book_to_check_out)
        today = datetime.date.today()
        week = datetime.timedelta(days=7)
        book_to_check_out.due_date = today + week
        book_to_check_out.format_due_date()
    return redirect ("/library")


@app.route("/library/<index>/delete", methods=['POST'])
def post_delete(index):
    index= int(index)
    book_to_delete = library.book_list[index]
    library.delete_book(book_to_delete)
    return redirect("/library")

@app.route("/library/add", methods=['POST'])
def post_add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    library.add_book(new_book)
    return redirect("/library")
