# Library Management System

library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author,
        "available": True
    }

    library.append(book)
    print("Book added successfully.")

def display_books():
    if not library:
        print("No books in the library.")
    else:
        for book in library:
            status = "Available" if book["available"] else "Borrowed"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")

def borrow_book():
    title = input("Enter book title to borrow: ")
    for book in library:
        if book["title"] == title and book["available"]:
            book["available"] = False
            print("Book borrowed successfully.")
            return
    print("Book not available.")

def return_book():
    title = input("Enter book title to return: ")
    for book in library:
        if book["title"] == title and not book["available"]:
            book["available"] = True
            print("Book returned successfully.")
            return
    print("Book not found or already returned.")

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
