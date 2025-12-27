library = {}

def add_book():
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")
    library[book_name] = {"author": author, "issued": False}
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books available.\n")
        return

    print("\nAvailable Books:")
    for book, info in library.items():
        status = "Issued" if info["issued"] else "Available"
        print(f"{book} by {info['author']} - {status}")
    print()

def issue_book():
    book_name = input("Enter book name to issue: ")
    if book_name in library and not library[book_name]["issued"]:
        library[book_name]["issued"] = True
        print("Book issued successfully!\n")
    else:
        print("Book not available or already issued.\n")

def return_book():
    book_name = input("Enter book name to return: ")
    if book_name in library and library[book_name]["issued"]:
        library[book_name]["issued"] = False
        print("Book returned successfully!\n")
    else:
        print("Invalid book name or book not issued.\n")

while True:
    print("---- Library Management System ----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using Library System.")
        break
    else:
        print("Invalid choice. Try again.\n")
