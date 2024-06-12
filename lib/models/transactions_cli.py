from transactions_db import TransactionsDB

def display_menu():
    print("\nLibrary Management System - Transactions")
    print("1. Lend Book")
    print("2. Return Book")
    print("3. List Transactions")
    print("4. Exit")

def main():
    transactions = TransactionsDB()
    transactions.create_tables()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title to lend: ")
            borrower = input("Enter the name of the borrower: ")
            transactions.lend_book(title, borrower)
        elif choice == '2':
            title = input("Enter book title to return: ")
            transactions.return_book(title)
        elif choice == '3':
            transactions.list_transactions()
        elif choice == '4':
            print("Exiting the transactions management system.")
            transactions.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
