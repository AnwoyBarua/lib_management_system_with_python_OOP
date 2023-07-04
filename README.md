# Library management system:
I have created this library management system using Python Object Oriented Programming concepts.

## Details:
There are two parent classes named: Book & Borrower. 
And one child class Library.

### Book class:
This class contains several functions like add_book & search_book.
#### add_book() function:
By calling this function you can add new books to your library. 
You can add more than one book at a time.
#### search_book() function :
Checks the availability status of a book.

### Brorrwer class:
This class contains borrow_book, return_book & create_account functions.
#### borrow_book() function:
Helps members to borrow books from the library if available. Note one can only borrow one book at a time.
(I will modify this one)
#### return_book() function:
Helps members to return their borrowed books.
#### create_account() function:
This one is for creating a new account. A unique member id will automatically be generated.

# Library class:
Finally library class inherits all the functionality of the above classes.
