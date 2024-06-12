import sqlite3

class TransactionsDB:
    def __init__(self, db_name="db/transactions.db"):
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

    def list_transactions(self):
        self.cursor.execute("""
            SELECT t.id, b.title, t.borrower, t.date_lent, t.date_returned
            FROM transactions t
            JOIN books b ON t.book_id = b.id
        """)
        transactions = self.cursor.fetchall()
        if not transactions:
            print("No transactions found.")
            return
        for transaction in transactions:
            status = f"Returned on {transaction[4]}" if transaction[4] else "Not returned yet"
            print(f"Transaction ID: {transaction[0]}, Book: '{transaction[1]}', Borrower: {transaction[2]}, Date Lent: {transaction[3]}, Status: {status}")

    def close(self):
        self.connection.close()
