from flask import render_template, request, redirect
from app import app
from models.book_list import book_list
from models.book import Book

@app.route("/")
def index():
    return render_template("index.html", title="Home", books=book_list)