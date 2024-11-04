# test_library_system.py
import unittest
from datetime import datetime, timedelta
from library import Book, Member, Library

class TestLibrarySystem(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        library.add_book("Book A", "Author A", 2)
        library.add_book("Book A", "Author A", 3)
        self.assertEqual(library.books["Book A"].copies, 5)

    def test_add_member(self):
        library = Library()
        library.add_member(1, "John Doe")
        library.add_member(2, "Jane Doe")
        self.assertIn(1, library.members)
        self.assertIn(2, library.members)

    def test_borrow_book_success(self):
        library = Library()
        library.add_book("Book A", "Author A", 1)
        library.add_member(1, "John Doe")
        result = library.borrow_book(1, "Book A")
        self.assertTrue(result)
        self.assertEqual(library.books["Book A"].copies, 0)

    def test_borrow_book_failure(self):
        library = Library()
        library.add_book("Book A", "Author A", 0)
        library.add_member(1, "John Doe")
        result = library.borrow_book(1, "Book A")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
