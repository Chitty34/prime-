#Library management system
'''Design a class Library to manage books. Implement the following methods.
add_book(title):Adds a book to the library.
remove_book(title):Removes a book if it exists.
is_available(title):Checks if a book is avalibility
list_books():Lists all books in the library'''
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, title):
        """Adds a book to the library."""
        if title not in self.books:
            self.books.append(title)
            print(f'Book "{title}" added to the library.')
        else:
            print(f'Book "{title}" already exists in the library.')

    def remove_book(self, title):
        """Removes a book if it exists."""
        if title in self.books:
            self.books.remove(title)
            print(f'Book "{title}" removed from the library.')
        else:
            print(f'Book "{title}" does not exist in the library.')

    def is_available(self, title):
        """Checks if a book is available in the library."""
        if title in self.books:
            print(f'Book "{title}" is available in the library.')
            return True
        else:
            print(f'Book "{title}" is not available in the library.')
            return False

    def list_books(self):
        """Lists all books in the library."""
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("No books available in the library.")


library = Library()
library.add_book("1984")
library.add_book("To Kill a Mockingbird")
library.list_books()
library.is_available("1984")
library.remove_book("1984")
library.is_available("1984")
library.list_books()

