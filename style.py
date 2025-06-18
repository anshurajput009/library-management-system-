class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'"{title}" added to library.')

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f'- {book.title} by {book.author} [{status}]')

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f'You borrowed "{book.title}".')
                return
        print("Sorry, book not available or doesn’t exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f'You returned "{book.title}".')
                return
        print("Book not found in borrowed list.")

# Sample Usage
library = Library()
library.add_book("Atomic Habits", "James Clear")
library.add_book("The Alchemist", "Paulo Coelho")

while True:
    print("\n1. Show Books\n2. Add Book\n3. Borrow Book\n4. Return Book\n5. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == '3':
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == '4':
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == '5':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")