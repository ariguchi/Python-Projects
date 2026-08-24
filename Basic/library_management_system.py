
class Books:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = 0

    def display_info(self):
        return " Title -->{}\n Author -->{}".format(self.title, self.author)

    def check_borrow(self):
        if self.is_borrowed == 0:
            print("You can borrow this book")
        else:
            print("You cannot borrow this book")

class Members:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed = 0

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

b1 = Books("Harry Potter", "JK Rowling")
m1 = Members("Conan", "1417")

library = Library()
library.add_books(b1)
library.add_member(m1)
