class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_lent:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' is either not in the library or currently lent out.")

    def lend_book(self, title, borrower):
        for book in self.books:
            if book.title == title and not book.is_lent:
                book.is_lent = True
                book.lent_to = borrower
                print(f"Book '{title}' lent to {borrower}.")
                return
        print(f"Book '{title}' is either not available or already lent out.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_lent:
                book.is_lent = False
                borrower = book.lent_to
                book.lent_to = None
                print(f"Book '{title}' returned by {borrower}.")
                return
        print(f"Book '{title}' is either not lent out or not in the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            status = "Available" if not book.is_lent else f"Lent out to {book.lent_to}"
            print(f"{book} - {status}")