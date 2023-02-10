from flask import render_template, request, redirect
from app import app
from models.book_list import book_list, delete_book, delete_book_index, add_book, check_out_book, check_book_in
from models.book import Book

@app.route("/library")
def index():
    return render_template("index.html", title="Home", book_list=book_list)

@app.route("/library/<index>")
def book_view(index):
    index = int(index)
    book_to_view = book_list[index]
    return render_template("book.html", title="Book", book=book_to_view, index=index)

@app.route("/library/<index>", methods=['POST'])
def post_update_check_status(index):
    index = int(index)
    book_to_check_out = book_list[index]
    if request.form["status"] == "CheckIn":
        book_to_check_out.checked_out = False
    else:
        book_to_check_out.checked_out = True
    return redirect ("/library")


@app.route("/library/<index>/delete", methods=['POST'])
def post_delete(index):
    index= int(index)
    book_to_delete = book_list[index]
    delete_book(book_to_delete)
    return redirect("/library")

@app.route("/library/add", methods=['POST'])
def post_add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect("/library")
