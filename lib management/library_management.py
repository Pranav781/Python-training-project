#create a libraray book mangement (do not use class, )use loop ,list statement function and operator
books = []

def add_book():
    title = input("Enter book title: ")
    books.append(title)
    print("Book added successfully.")

def remove_book():
    title = input("Enter book title to delete: ")
    if title in books:
        books.remove(title)
        print("Book removed.")
    else:
        print("Book not found.")

def view_books():
    if not books:
        print("The library is empty.")
    else:
        print("\n--- Library Collection ---")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}")

def search_book():
    title = input("Enter book title to search: ")
    if title in books:
        print(f"'{title}' is available in the library.")
    else:
        print(f"'{title}' is not in our collection.")

def main():
    while True:
        print("\n1. Add Book\n2. Remove Book\n3. View All Books\n4. Search Book\n5. Exit")
        a = input("Select an option: ")
        
        if a=="1":
            add_book()
        elif a=="2":
            remove_book()
        elif a == "3":
            view_books()
        elif a=="4":
            search_book()
        elif a=="5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()