
class Books:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = 0

    def display_info(self):
        return " Title -->{}\n Author -->{}".format(self.title, self.author)

class Members:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def member_details(self):
        return "Member: {} | ID: {}".format(self.name, self.id)   

class Library:

    def __init__(self ):
        self.books = []
        self.members = []

    def add_books(self, books):
        self.books.append(books)

    def add_member(self, members):
        self.members.append(members)

    def borrow_book(self, books, members):
        if books.is_borrowed == 0:
            members.borrowed_books.append(books)
            books.is_borrowed = 1
        else:
            print("The book is currently unavailable")

b1 = Books("Harry Potter", "JK Rowling")
m1 = Members("Conan", "1417")

library = Library()
library.add_books(b1)
library.add_member(m1)

library.borrow_book(b1,m1)
library.borrow_book(b1,m1)

