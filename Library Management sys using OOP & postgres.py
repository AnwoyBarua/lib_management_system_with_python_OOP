# ###########
# # Parent class Book, Borrower. 
# # Child class Library.
# ###########
# ## Book class contains ===>
# ## function --> add_book()
### This function will help you to add one or more books.
# ## function --> search_book()
### This function is used to check whether a book is available.
# ###########
# ## Borrwer class contains ===>
# ## function --> borrow_book() 
### This function is used to help members borrow books they want. Note: they can only borrow one book at a time.
# ## function --> return_book()
### This function helps members to return books that they borrowed.
# # function create_account()
### create a new user account.

import csv
import pandas as pd

# Change the file path while running this code.
book_url = "E:\Programming\python\OOP projects\Data\\books.csv"
borrower_url = "E:\Programming\python\OOP projects\Data\\borrowers.csv"

class Book:
    
    def __init__(self):
        pass

    def add_book(self):
        '''
            This class can be used to add new books to your library. It can take one or more than one booklist.
        '''
        books = []
        n = int(input("How many books do you want to insert?\n"))
        for i in range(n):
            books.append({
                'title' : input("enter book title:  "),
                'author': input("enter author name:  "),
                'isbn': input('enter isbn serial no.:  '),
                'pub_year': input('enter publication year:  '),
                'available_status' : True
                })
            
        header = ['title', 'author', 'isbn', 'pub_year', 'available_status']   
        with open(book_url, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames= header)
            writer.writerows(books)
            f.close()
        print("\nBook sucessfully added.\n")

    def search_book(self):
        '''
            This class will be used to search for book on your library.
            Version - 01
        '''
        book_list = csv.reader(open(book_url, 'r'))
        title = input("enter book name: ")
        author = input('enter author name: ')
        for i in book_list:
            if i[0].lower() == title.lower() and i[1]== author.lower():
                print("\nBook Available.\n")
                return
        print("\nNot Found!!!\n")

class Borrower:
    books = pd.read_csv(book_url)
    borrowers = pd.read_csv(borrower_url)

    def __init__(self):
         pass
 
    def borrow_book(self):
        '''
            This function is going to help you borrow book from library.
        '''
        try:
            borrower_id = int(input("enter your member id: "))
        except:
            print("\n!!! Attention !!! you didn't enter your member id Enter again.\n")
            return
        
        b = Borrower.borrowers.loc[Borrower.borrowers['borrower_id'] == borrower_id]
        # logic that will help members to borrow book.
        if b.shape[0] != 0:
            try:
                title, author = input("Enter book title and author: ").split(",")
            except:
                print("\n!!! Warning !!! \nEnter title and author comma separated.\n")
                return
            
            if any((Borrower.books['title']== title ) & (Borrower().books['author'] == author) & (Borrower().books["av_status"] == 'yes')):
                
                print("\nBook available. You can collect your book from library manager.\n")
                # there is only one book of each title. Now it's not available.
                # make borrowed book unavailable.
                Borrower.books.loc[Borrower.books["title"] == title , "av_status"] = 'no'
                Borrower.books.to_csv(book_url, index = False)
                # one member can borrow one book at a time. So, make borrwed status yes
                Borrower.borrowers.loc[Borrower.borrowers['borrower_id'] == borrower_id, "b_status"] = "yes"
                Borrower.borrowers.to_csv(borrower_url, index = False)
                return
            print("\n")
            print("\nYou might have misspelled or book is not available right now. Try again!\n")
            return
        print("\nYour account no is not valid. retype or create an account.\n")

    def return_book(self):
        '''
            This function will help members to return their books.
        '''
        try:
            borrower_id = int(input("Enter your member id: "))
        except:
            print("\nEnter your member id.\n")
            return
        
        b = Borrower.borrowers.loc[Borrower.borrowers['borrower_id'] == borrower_id]
        if b.shape[0] != 0:
            try:
                title, author = input("Enter title and author: ").split(",")
            except:
                print("\n!!! Warning!!!\nEnter title and author comma separated.\n")
                return

            if any((Borrower.books['title']== title ) & (Borrower.books['author'] == author)):
                Borrower.books.loc[Borrower.books["title"] == title , "av_status"] = 'yes'
                Borrower.books.to_csv(book_url,  index= False)

                Borrower.borrowers.loc[Borrower.borrowers['borrower_id'] == borrower_id, "b_status"] = "no"
                Borrower.borrowers.to_csv(borrower_url, index= False)
                print("Book returned...")
                return            
            print("Wrong title or author.")
            return
        print("Wrong member id.")


    def create_account(self):
        try:
            name, age, gender,phone = input("Enter name, age, gender & phone comma separated: ").split(",")
        except:
            print("\n!!!Warning!!!\nEnter all the information needed.\n")
            return
    
        b_status = 'no'
        # id will be automatically generated by the following code
        b_id = Borrower.borrowers["borrower_id"].iloc[-1] + 1
        member = [b_id, name, age, gender,phone, b_status]

        with open(borrower_url, 'a', newline= '') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(member)
            f.close()
        print(f"\nSuccessfully Account Created...\n Your member id is: {b_id}")
        


class Library(Book, Borrower):
    def __init__(self):
        pass


#### Command Line Interface (CLI)

def display_menu():
    print("Welcome to the Library Management System!")
    print("1. Add a book")
    print("2. Search a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Create an account")
    print("6. Exit")

def add_book():
    Library().add_book()

def search_book():
    Library().search_book()

def borrow_book():
    Library().borrow_book()

def return_book():
    Library().return_book()

def create_account():
    Library().create_account()
# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        print("\n")
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        print("\n")
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        create_account()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        
