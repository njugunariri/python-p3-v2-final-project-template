#!/usr/bin/env python3
# lib/debug.py

from models import CONN, CURSOR
import ipdb
from models.library_db import LibraryDB
from models.transactions_db import TransactionsDB

# Instantiate the database classes
library = LibraryDB()
transactions = TransactionsDB()

# Sample data for debugging
library.add_book("Sample Book 1", "Author 1")
library.add_book("Sample Book 2", "Author 2")
transactions.lend_book("Sample Book 1", "Borrower 1")

# Set an IPDB breakpoint
ipdb.set_trace()

# Debug actions
# Example of listing all books
library.list_books()

# Example of listing all transactions
transactions.list_transactions()

# Clean up and close the connection
library.close()
transactions.close()
