class Book1:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []
        self.book_id_counter = 1

    def add_book(self, title, author, genre, isbn):
        book = Book1(title, author, genre, isbn)
        book.book_id = self.book_id_counter
        self.book_id_counter += 1
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    def display_books(self, page=1, books_per_page=10):
        if not self.books:
            print("The library is empty.")
        else:
            total_books = len(self.books)
            total_pages = (total_books + books_per_page - 1) // books_per_page
            if page < 1 or page > total_pages:
                print("Invalid page number. Please try again.")
                return

            start_idx = (page - 1) * books_per_page
            end_idx = min(start_idx + books_per_page, total_books)

            print(f"Books in the library (Page {page}/{total_pages}):")
            print("-" * 102)
            print("| {:^5} | {:^40} | {:^20} | {:^15} | {:^20} |".format("ID", "Title", "Author", "Genre", "ISBN"))
            print("-" * 102)
            for book in self.books[start_idx:end_idx]:
                title = book.title[:37] + "..." if len(book.title) > 37 else book.title
                author = book.author[:18] + "..." if len(book.author) > 18 else book.author
                print("| {:^5} | {:<40} | {:<20} | {:<15} | {:<20} |".format(book.book_id, title, author, book.genre, book.isbn))
            print("-" * 102)

    def inventory(self):
        notable_books = [
            ("To Kill a Mockingbird", "Harper Lee", "Fiction", "978-0061120084"),
            ("1984", "George Orwell", "Science Fiction", "978-0451524935"),
            ("The Great Gatsby", "F. Scott Fitzgerald", "Classic", "978-0743273565"),
            # Add more notable books here
            # ("Book Title", "Author", "Genre", "ISBN"),
        ]

        for book_info in notable_books:
            title, author, genre, isbn = book_info
            self.add_book(title, author, genre, isbn)

def main():
    library = Library()

    # Add notable books to the library
    library.inventory()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, genre, isbn)
        elif choice == "2":
            page = int(input("Enter the page number (1 for the first page): "))
            library.display_books(page=page)
        elif choice == "3":
            title = input("Enter the title of the book: ")
            library.search_book(title)
        elif choice == "4":
            author = input("Enter the author of the book: ")
            library.search_book(author)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
