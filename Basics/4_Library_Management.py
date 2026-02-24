books = {}
issued_books = {}

def add_book():
    name = input("Enter book name: ").strip()
    qty = int(input("Enter quantity: "))
    books[name] = books.get(name, 0) + qty
    print("Book added successfully!")

def view_books():
    if not books:   
        print("No books available.")
    else:
        for b, q in books.items():
            print(f"{b} -> {q} copies")

def issue_book():
    name = input("Enter book name: ").strip()
    user = input("Enter user name: ").strip()

    if books.get(name, 0) > 0:
        books[name] -= 1

        if name not in issued_books:
            issued_books[name] = []

        issued_books[name].append(user)
        print("Book issued successfully!")
    else:
        print("Book not available!")

def return_book():
    name = input("Enter book name: ").strip()
    user = input("Enter user name: ").strip()

    if name in issued_books and user in issued_books[name]:
        books[name] += 1
        issued_books[name].remove(user)

        if not issued_books[name]:
            issued_books.pop(name)

        print("Book returned successfully!")
    else:
        print("Invalid return!")

def view_issued_books():
    if not issued_books:
        print("No books are issued.")
    else:
        for book, users in issued_books.items():
            print(f"{book} -> Issued to {', '.join(users)}")

while True:
    print("\n1.Add Book  2.View Books  3.Issue Book  4.Return Book  5.View Issued  6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        view_issued_books()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")