from flask import render_template, request, redirect
from app import app
from models.book_list import book_list
from models.book import Book

@app.route("/library")
def index():
    return render_template("index.html", title="Home", book_list=book_list)

@app.route("/library/<index>")
def book_view(index):
    index = int(index)
    book_to_view = book_list[index]
    return render_template("book.html", title="Book", book=book_to_view, index=index)