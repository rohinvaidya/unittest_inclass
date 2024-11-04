from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed_count = 0

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            self.borrowed_count += 1
            return True
        return False

    def return_book(self):
        self.copies += 1

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book):
        if book.borrow():
            due_date = datetime.now() + timedelta(days=14)
            self.borrowed_books[book.title] = due_date
            return True
        return False
    
    
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, copies=1):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)

    def add_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id, title):
        member = self.members.get(member_id)
        book = self.books.get(title)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, title):
        member = self.members.get(member_id)
        book = self.books.get(title)
        if member and book:
            return member.return_book(book)
        return False

    def get_overdue_members(self):
        return [member.name for member in self.members.values() if member.has_overdue_books()]