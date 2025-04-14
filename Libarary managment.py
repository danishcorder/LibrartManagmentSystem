class Book:
    def __init__(self,title,author,isbn,is_borrowed,AccessionNo,publicatio_date,genre):
        self.AccessionNo=AccessionNo
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed = False
        self.genre=genre
        self.publicatio_date=publicatio_date

    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            return True
        return False

    def get_book_info(self):
        return f"Title:{self.title} written by {self.author} ISBN:{self.isbn} and Accession no : {self.AccessionNo},Genre:{self.genre},Publication Date:{self.publicatio_date}"

    def is_available(self):
        return not self.is_borrowed
    
class User:
    max_borrow_limit=3
    def __init__(self,name,user_id,contact_info):
        self.name=name
        self.user_id=user_id
        self.contact_info=contact_info
        self.borrowed_books=[]
        self.fine=0

    def __str__(self):
        return f"Name :{self.name},ID{self.user_id}"

    def borrow_book(self,book):
        if len(self.borrowed_books)>=User.max_borrow_limit:
            print(f"Sorry {self.name} has already borrowed {User.max_borrow_limit} books for this month")
            return False

        if book.borrow():
            self.borrowed_books.append(book)    
            return  True
        return False
        
    def return_book(self,book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False
    def pay_fine(self,amount):
        if amount>=self.fine:
            print(f"{self.name} paid the full time fine of ${self.fine}")
            self.fine=0
        else:
            self.fine-=amount
            print(f"{self.name} paid amount ${amount} \n Remaning Amount : ${self.fine}") 

    def get_user_info(self):
        return f" User :{self.name},Contact:{self.contact_info} Fine Due:{self.fine}"    

    def view_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"Borrowed Books:{self.borrowed_books}")       
    
    
class Labirarian:
    def  __init__ (self,name,employe_id,assinged_section):
        self.assinged_section=assinged_section
        self.name=name
        self.employe_id=employe_id
    
    def search_book(self,book,title):
        self.book=book
        self.title=title
        return [book for book in books if title.lower() in book.title.lower() ]
    
    def calculate_fine(self,over_due):
        return over_due*1
    
   

class LibrararyaManagmentsystem:
    def __init__(self):
        self.books=[]
        self.users=[]
        self.overdue_fine_rate=1
        self.borrow_limit=3

    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,book):
        self.books.remove(book)
    def register_user(self,user):
        self.users.append(user)
 
library=LibrararyaManagmentsystem()

print("*************************************************")
book1=Book("Holy prophert Muhammad saw","Molana shibli nomani","123456789","8978","1234567","2021","123323333")
library.add_book(book1)
print("*************************************************")
print(book1.get_book_info())
print("*************************************************")
book2=Book("Vector Tensor","Shivaram","567890","6787678","234567","2021","123323333")
library.add_book(book2)
print("*************************************************")
print(book2.get_book_info())
print("*************************************************")

book3=Book("Medium","Dr.Athar kharal ","67687","675434","45677","2021","123323333")
library.add_book(book3)
print("*************************************************")
print(book3.get_book_info())
print("*************************************************")
book4=Book("Git","Ansar","344565","80988","88999","2021","123323333")
library.add_book(book4)
print("*************************************************")
print(book4.get_book_info())
print("*************************************************")

user1=User("Muhammd Danish","16","khan@gamil.com")
print(user1.get_user_info())
library.register_user(user1)
user1.pay_fine(6)
user1.pay_fine(10)

user1.borrow_book(book1)
user1.return_book(book1)
user1.borrow_book(book2)
user1.return_book(book2)

user1.borrow_book(book3)
user1.return_book(book3)
user1.borrow_book(book4)
user1.return_book(book4)

print("*************************************************")
labriria=Labirarian("Nasir",234,"Tecnology")

print("*************************************************")
books=[book1,book2,book3,book4] 
print("*************************************************")

user1.borrow_book(book1)
print("*************************************************")
print("*************************************************")
user1.borrow_book(book2)
print("*************************************************")
print("*************************************************")
user1.borrow_book(book3)
print("*************************************************")
print("*************************************************")
user1.borrow_book(book4)
print("*************************************************")
print("*************************************************")


if user1.borrow_book(book1):
    print("*************************************************")
    print(f"{user1.name} borrowed '{book1.title}'")
    print("*************************************************")
if user1.return_book(book1):
    print("*************************************************")
    print(f"{user1.name} returned '{book1.title}'")
    print("*************************************************")

results=labriria.search_book(books,"1987")

if user1.borrow_book(book2):
    print("*************************************************")
    print(f"{user1.name} borrowed '{book2.title}'")
    print("*************************************************")
if user1.return_book(book2):
    print("*************************************************")
    print(f"{user1.name} returned '{book2.title}'")
    print("*************************************************")

results=labriria.search_book(books,"Github")
print("*************************************************")

if user1.borrow_book(book3):
    print("*************************************************")
    print(f"{user1.name} borrowed '{book3.title}'")
    print("*************************************************")
if user1.return_book(book3):
    print("*************************************************")
    print(f"{user1.name} returned '{book3.title}'")
print("*************************************************")
results=labriria.search_book(books,"Github")
print("*************************************************")
if user1.borrow_book(book4):
    print("*************************************************")
    print(f"{user1.name} borrowed '{book4.title}'")
    print("*************************************************")
if user1.return_book(book4):
    print("*************************************************")
    print(f"{user1.name} returned '{book4.title}'")

results=labriria.search_book(books,"Github")
print("*************************************************")
print(f"Fine for 3 overdue days :${labriria.calculate_fine(3)}")

print("*************************************************")
print("*************************************************")
print("Thank You ! Have a nice day")


