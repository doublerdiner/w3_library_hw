from datetime import date
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = False
        self.due_date = None

    
    def format_due_date(self):
        date = str(self.due_date)
        new = date.split("-")
        year = new[0]
        month = new[1]
        day = new[2]
        self.due_date = f"{day}/{month}/{year}"