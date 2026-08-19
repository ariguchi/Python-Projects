
class Books:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = false

class Members:

    def __init__(self, name, id):
        self.name = name
        self.id = id

class Library:

    def __init__(self ):
        self.books = []
        self.members = []
