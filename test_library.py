# test_library_system.py
import unittest
from datetime import datetime, timedelta
from library import Book, Member, Library

class TestLibrarySystem(unittest.TestCase):

    # tests adding new and existing books, verifying that copies increment correctly
    def test_add_book(self):
        library = Library()
        library.add_book("Book A", "Author A", 2)
        library.add_book("Book A", "Author A", 3)
        self.assertEqual(library.books["Book A"].copies, 5)
    
    # verifies that members are added to the library
    def test_add_member(self):
        library = Library()
        library.add_member(1, "John Doe")
        library.add_member(2, "Jane Doe")
        self.assertIn(1, library.members)
        self.assertIn(2, library.members)

    # tests successful borrowing of a book by a member
    def test_borrow_book_success(self):
        library = Library()
        library.add_book("Book A", "Author A", 1)
        library.add_member(1, "John Doe")
        result = library.borrow_book(1, "Book A")
        self.assertTrue(result)
        self.assertEqual(library.books["Book A"].copies, 0)

    # tests borrowing a book when no copies are available
    def test_borrow_book_failure(self):
        library = Library()
        library.add_book("Book A", "Author A", 0)
        library.add_member(1, "John Doe")
        result = library.borrow_book(1, "Book A")
        self.assertFalse(result)

    def test_return_book(self):
        library = Library()
        library.add_book("Book A", "Author A", 0)
        library.add_member(1, "John Doe")
        result = library.return_book(1, "Book A")
        self.assertTrue(result)

    def test_return_book_failure(self):
        library = Library()
        result = library.return_book(1, "Book A")
        self.assertFalse(result)

    def test_add_member_failure(self):
        library = Library()
        library.add_member(1, "John Doe")
        self.assertIn(1, library.members)
        self.assertNotIn(3, library.members)

if __name__ == "__main__":
    unittest.main()


