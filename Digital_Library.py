import random
class Login: 
    students=[]
    borrowed_book={}
    current_student_id = None
    def register(self):
        user = input("Press 1 register account Press 2 login:")
        if user == "1":
            # name
            while True:
                try:
                    name = input("Name: ")
                    if not name.replace(" ", "").isalpha(): 
                        raise ValueError("Please input name alphabet!")
                    break
                except ValueError as e:
                    print(e)
                    continue
            #Student ID       
            while True:
                try:
                    student_id = int(input("Student ID: "))
                    break
                except ValueError:
                    print("input only number!")
                    continue
            #CINC
            while True:
                try:
                    cnic = int(input("CNIC Number: "))
                    break
                except ValueError:
                    print("input only number!")
                    continue
            #OTP
            num = random.randint(1000,9999)
            print(f"Security Alert: Your verification code is {num}")
            while True:
                try:
                    otp = int(input("Enter OTP: "))
                    if num == otp:
                        print("Your account successfully!")
                        student = {
                            "name": name,
                            "student ID": student_id,
                            "cnic": cnic
                        }
                        Login.students.append(student)
                        return "Registration Completed!"
                        break
                    else:
                        print("Wrong OTP!!!!")
                except ValueError:
                    print("invalid input only number!")
        elif user == "2":
            #name
            while True:
                try: 
                    names =input('enter your name:')
                    if not names.replace(" ", "").isalpha(): 
                        raise ValueError("Please input name alphabet!")
                    found = False
                    for student in Login.students:
                        if student["name"] == names:
                            found= True
                            break
                    if found:
                        break
                    else: 
                        print("invalid name")
                            
                except ValueError as e:
                    print(e)
                    continue
            
                           
                    
            #Student ID
            while True:
                try:
                    student_id = int(input('enter your ID'))
                    break
                except ValueError:
                    print("valid input only number")
                    continue
            for student in Login.students:
                if student["student ID"] == student_id:
                    Login.current_student_id = student_id
                    print("welcome to library")
                    main()
                    break
            else:
                print("wrong Your ID")
        else:
            return "Invalid Choise"
            
class Book:
    def __init__(self, title, author, book_id, total_copies):
        self.__title = title
        self.__author = author
        self.__book_id = book_id
        self.__total_copies = total_copies

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_book_id(self):
        return self.__book_id

    def get_total_copies(self):
        return self.__total_copies

    # Setters
    def set_total_copies(self, copies):
        self.__total_copies = copies


class Library:
    def __init__(self):
        self.__Books = [
            Book("Python Crash Course", "Eric Matthes","BS001", 5),
            Book("Automate the Boring Stuff", "Al Sweigart", "BS002", 3),
            Book("Learning Python", "Mark Lutz", "BS003", 4),
            Book("Clean Code", "Robert C. Martin", "BS004", 6),
            Book("The Pragmatic Programmer", "Andy Hunt", "BS005", 5),
            Book("Think Python", "Allen B. Downey", "BS006", 4),
            Book("Fluent Python", "Luciano Ramalho", "BS007", 2),
        ]

    def add_book(self, book):
        self.__Books.append(book)

    def view_book(self):
        for book in self.__Books:
            print(f"Title: {book.get_title()} Author: {book.get_author()} "
                  f"Book ID: {book.get_book_id()} Total Book: {book.get_total_copies()}")

    def borrow_book(self, title_book):
        student_id = Login.current_student_id
        for book in self.__Books:
            if book.get_title().lower() == title_book.lower():
                if book.get_total_copies() > 0:
                    book.set_total_copies(book.get_total_copies() - 1)
                    Login.borrowed_book.setdefault(student_id, []).append(book.get_book_id())
                    print("Successfully borrowed book")
                else:
                    print('No copies available')
                break
        else:
            print("This book is not in the library!")


    def return_book(self, books_id):
        student_id = Login.current_student_id
        for book in self.__Books:
            if book.get_book_id() == books_id:
                if books_id in Login.borrowed_book.get(student_id, []):
                    Login.borrowed_book[student_id].remove(books_id)
                    book.set_total_copies(book.get_total_copies() + 1)
                    print("Thanks for returning the book!")
                else:
                    print("You did not borrow this book!")
                break
        else:
            print("Your book ID doesn't match!")

    def search_title(self, s_title):
        found=False
        for book in self.__Books:
            if book.get_title().lower() == s_title.lower():
                print(f"{book.get_title()} by {book.get_author()}")
                found=True
        if not found:
            print("Please correct input!! ")

    def search_author(self, s_author):
        found = False
        for book in self.__Books:
            if book.get_author().lower() == s_author.lower():
                print(f"{book.get_title()} by {book.get_author()}")
                found=True
        if not found:
            print("Please correct input!!")
    def check_book_id(self,book_id):
        for book in self.__Books:
            if book.get_book_id() == book_id:
                return True   
        return False   
        
def main():
    library = Library()
    while True:
        print("Press 1 Add book")
        print("Press 2 view book")
        print("Press 3 borrow_book")
        print("Press 4 return book")
        print("press 5 search by title")
        print("Press 6 search by author ")
        print("Press 7 exit")
        choise = input("choose to 1to7: ")
        if choise == "1":
            title = input("Enter Book name:")
            author = input("Enter Author name")
            book_id = input("Enter book ID").upper()
            if library.check_book_id(book_id):
                print("This Book Already Exists")
            else:       
                while True:
                    try:
                        total_copies = int(input("Total copies"))
                        break
                    except ValueError:
                        print("valid input only number!")
           
                library.add_book(Book(title, author,book_id, total_copies))
                print("Book added successfully!")
        elif choise == "2":
            library.view_book()
        elif choise == "3":
            title_book = input("Enter title book")
            library.borrow_book(title_book)
        elif choise == '4':
            books_id = input("book id ").upper()
            library.return_book(books_id)
        elif choise == '5':
            s_title = input("search by title ")
            library.search_title(s_title)
        elif choise == '6':
            s_author = input("search by author")
            library.search_author(s_author)
        elif choise == "7":
            print("Thanks you visit Library")
            break
        else:
            print("Please Correct Chose Number !!!")
obj=Login()
print(obj.register())



