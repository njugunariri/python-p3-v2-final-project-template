import sqlite3

class LibraryDB:
    def __init__(self, db_name="db/library.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_lent INTEGER NOT NULL DEFAULT 0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                borrower TEXT,
                date_lent TEXT,
                date_returned TEXT,
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)
        self.connection.commit()

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.connection.commit()
        print(f"Book '{title}' added to the library.")

    def remove_book(self, title):
        self.cursor.execute("DELETE FROM books WHERE title = ? AND is_lent = 0", (title,))
        if self.cursor.rowcount > 0:
            print(f"Book '{title}' removed from the library.")
        else:
            print(f"Book '{title}' is either not in the library or currently lent out.")
        self.connection.commit()

    def lend_book(self, title, borrower):
        self.cursor.execute("SELECT id FROM books WHERE title = ? AND is_lent = 0", (title,))
        book = self.cursor.fetchone()
        if book:
            book_id = book[0]
            self.cursor.execute("UPDATE books SET is_lent = 1 WHERE id = ?", (book_id,))
            self.cursor.execute("INSERT INTO transactions (book_id, borrower, date_lent) VALUES (?, ?, DATE('now'))", (book_id, borrower))
            print(f"Book '{title}' lent to {borrower}.")
        else:
            print(f"Book '{title}' is either not available or already lent out.")
        self.connection.commit()

    def return_book(self, title):
        self.cursor.execute("SELECT id FROM books WHERE title = ? AND is_lent = 1", (title,))
        book = self.cursor.fetchone()
        if book:
            book_id = book[0]
            self.cursor.execute("UPDATE books SET is_lent = 0 WHERE id = ?", (book_id,))
            self.cursor.execute("UPDATE transactions SET date_returned = DATE('now') WHERE book_id = ? AND date_returned IS NULL", (book_id,))
            print(f"Book '{title}' returned.")
        else:
            print(f"Book '{title}' is either not lent out or not in the library.")
        self.connection.commit()

    def list_books(self):
        self.cursor.execute("SELECT title, author, is_lent FROM books")
        books = self.cursor.fetchall()
        if not books:
            print("No books in the library.")
            return
        for book in books:
            status = "Available" if book[2] == 0 else "Lent out"
            print(f"'{book[0]}' by {book[1]} - {status}")

    def close(self):
        self.connection.close()
