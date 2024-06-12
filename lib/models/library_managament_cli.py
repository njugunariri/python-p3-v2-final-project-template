from library_db import LibraryDB
from transactions_db import TransactionsDB

def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. List Books")
    print("6. List Transactions")
    print("7. Exit")

def main():
    library = LibraryDB()
    transactions = TransactionsDB()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == '3':
            title = input("Enter book title to lend: ")
            borrower = input("Enter the name of the borrower: ")
            transactions.lend_book(title, borrower)
        elif choice == '4':
            title = input("Enter book title to return: ")
            transactions.return_book(title)
        elif choice == '5':
            library.list_books()
        elif choice == '6':
            transactions.list_transactions()
        elif choice == '7':
            print("Exiting the library management system.")
            library.close()
            transactions.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
