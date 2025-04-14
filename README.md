**Library Management System** : This is a simple object-oriented library management system written in Python. It allows you to manage books, users (like library members), and basic librarian operations such as borrowing, returning, and searching for books.

**✅ Main Features:**

1.** Book Management:** Each book has details: title, author, ISBN, accession number, genre, publication date, and borrow status.

You can:

Borrow a book (if it's not already borrowed).

Return a book.

Get the book's details.

Check if the book is available.

2.** User Management**: Each user has a name, ID, contact info, a fine balance, and a list of borrowed books.

Users can:

Borrow up to 3 books.

Return books they’ve borrowed.

View borrowed books.

Pay fines (partial or full).

View their account info.

3.** Librarian (Labirarian):** The librarian class can:

Search for books by title from a given book list.

Calculate overdue fines (simple flat rate: $1 per day overdue).

4.** Library System:** A central system (named LibrararyaManagmentsystem) handles:

Adding and removing books.

Registering users.

Holding all users and books in lists.

**🧠 Concepts Used:** Object-Oriented Programming (OOP): Classes like Book, User, Labirarian, and LibrararyaManagmentsystem.

Encapsulation: Book borrowing/returning is handled inside the class.

Basic data validation: Limits on borrowing, fine handling.

Lists: For tracking users and books.

**🛠️ Potential Uses**: Good for small-scale library or personal use.

Can be extended for real use by adding:

GUI (Tkinter, PyQt)

Database support (SQLite, MySQL)

Web version using Flask/Django
