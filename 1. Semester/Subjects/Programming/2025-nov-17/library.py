# login DONE
# check login DONE
# if existing login send to logged in DONE
# if not existing send to register DONE
# register DONE
# needs a username & password DONE
# check if already existing  DONE
# Logged in menu DONE
# search function DONE
# borrow/return books DONE
# show what you have borrowed DONE
# show all books and if its borrowed or not
# log out DONE

# search function
# checks for author DONE
# check for name DONE
# tells if book is already borrowed DONE
# match function if misspelled

# borrow/deliver system
# checks for borrowed books DONE
# checks if book is borrowed DONE

# Show my borrowed list
# listing from borrowed books under name DONE

# show all books DONE

# Log out DONE

from time import sleep
import hashlib
import json
import os

# path = os.getcwd() + r"/Fag\Programering\2025-nov-17"
path = os.getcwd()


def login(accounts):
    print("Welcome to the library\nYou need to login to continue")
    sleep(2)
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in accounts["usernames"]:
        index = accounts["usernames"].index(username)

        if encoding(password) == accounts["passwords"][index]:
            loggedIn(username)
        else:
            makeAcc = input(
                "Username or Password was wrong\nDo you want to register for a account?\n(yes/no)\n"
            )
            while makeAcc not in ("yes", "no"):
                print("invalid input")
            if makeAcc == "yes":
                register(accounts, "")
                loggedIn(username)
    elif username not in accounts["usernames"]:
        makeAcc = input(
            "Username or Password was wrong\nDo you want to register for a account?\n(yes/no)\n"
        )
        while makeAcc not in ("yes", "no"):
            print("invalid input")
        if makeAcc == "yes":
            register(accounts, "")
            loggedIn(username)


def register(accounts, nothing):
    print("To create an account enter the following.")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username in accounts["usernames"]:
        print("Username already taken")
        register(accounts, "")
    else:
        accounts["usernames"].append(username)
        password = encoding(password)
        accounts["passwords"].append(password)
        print("Account created")
        sleep(2)
        updateAccounts(accounts)
        return accounts, username


def encoding(password):
    password = hashlib.sha256(
        hashlib.sha256(password.encode()).hexdigest().encode()
    ).hexdigest()
    return password


def loggedIn(username):
    while username:
        print("#######################################################")
        print(f"successfully logged in as {username}")
        print("""You now have the following options: 
        1 = find a book
        2 = borrow a book
        3 = return a book
        4 = show all books
        5 = show all books and if they are borrowed or not
        6 = show my borrowed books
        7 = logout""")
        pick = input("Enter choice here: ")
        while pick not in ("1", "2", "3", "4", "5", "6", "7", "999"):
            pick = input("invalid input\nEnter choice here: ")
        if pick == "1":
            findBook()
        if pick == "2":
            borrowBook(username)
        if pick == "3":
            returnBook(username)
        if pick == "4":
            showBooks(False)
        if pick == "5":
            showBooks(True)
        if pick == "6":
            showMyBorrowedBooks(username)
        if pick == "7":
            pick = None
            return
        pick = None


def getBooks():
    with open(f"{path}/books.json", "r", encoding="UTF-8") as f:
        books = json.load(f)
        return books


def getAccounts():
    with open(f"{path}/accounts.json", "r", encoding="UTF-8") as f:
        accounts = json.load(f)
        return accounts


def updateBooks(books):
    with open(f"{path}/books.json", "w", encoding="UTF-8") as f:
        json.dump(books, f)


def updateAccounts(accounts):
    with open(f"{path}/accounts.json", "w", encoding="UTF-8") as f:
        json.dump(accounts, f)


def showBooks(check):
    with open(f"{path}/books.json", "r", encoding="UTF-8") as f:
        books = json.load(f)
    if not check:
        for title in books.keys():
            print(title)
    if check:
        for title, information in books.items():
            if information["borrowed_by"]:
                print(f"Title: {title} is currently: Borrowed")
            if not information["borrowed_by"]:
                print(f"Title: {title} is currently: Available")
    sleep(2)


def findBook():
    books = getBooks()
    print("""To find a book by title press 1 
To find a book by author press 2""")
    search = input("Enter choice here: ")
    if search == "1":
        search = input("Enter the books title here: ")
        for title in books.keys():
            if search == title:
                if books[title]["borrowed_by"] is None:
                    print(
                        f"{title} was found in the system and is currently available!"
                    )
                    sleep(2)
                    return
                if books[title]["borrowed_by"] is not None:
                    print(
                        f"{title} was found in the system and is currently borrowed..."
                    )
                    sleep(2)
                    return
        print(f"No matches found for {search}")
        sleep(1)
    if search == "2":
        search = input("Enter the authors name here: ")
        for title, book in books.items():
            if search in book["Author"]:
                print(f"Match found for {search} with the title: {title}")
                sleep(2)
                return
        print(f"No matches found for {search}")
        sleep(2)


def returnBook(username):
    books = getBooks()
    yourBorrowedBooks = []
    for book, borrowedBy in books.items():
        if borrowedBy["borrowed_by"] == username:
            yourBorrowedBooks.append(book)
    if len(yourBorrowedBooks) == 0:
        print("No borrowed books was found under your username")
        sleep(2)
        return
    else:
        print("Your currently borrowed books are:\n")
        for book in yourBorrowedBooks:
            print(book)
            toReturn = input(
                "Enter the title of the books you want to return or q to exit\nEnter input here: "
            )
            while toReturn not in (yourBorrowedBooks, "q"):
                toReturn = input(
                    "Invalid input\nEnter the title of the books you want to return or q to exit\nEnter input here: "
                )
            if toReturn == "q":
                return
            if toReturn in yourBorrowedBooks:
                books[toReturn]["borrowed_by"] = None
                updateBooks(books)
                print(f"{toReturn} has been returned")
                sleep(2)


def borrowBook(username):
    booking = "ACTIVE"
    while booking:
        print(
            "You have the following options\n to see a list of all books press 1\nTo borrow a book enter its name\nTo exit press 'q'\nEnter choice here: "
        )
        toDo = input("")
        if toDo == "1":
            showBooks(True)
        if toDo == "q":
            booking = False
        else:
            books = getBooks()
            if toDo in books.keys():
                if not books[toDo]["borrowed_by"]:
                    borrowedBy = username
                    books[toDo]["borrowed_by"] = borrowedBy
                    updateBooks(books)
                    print(f"{toDo} is now booked")
                    sleep(2)
                else:
                    print("That book is already borrowed...")


def showMyBorrowedBooks(username):
    books = getBooks()
    toPrint = "Books borrowed by you are: "
    for book, information in books.items():
        if information["borrowed_by"] == username:
            toPrint += "\n" + book
    if toPrint == "Books borrowed by you are: ":
        print("No books found under your name...")
        sleep(2)
    else:
        print(toPrint)
        sleep(2)


def main():
    accounts = getAccounts()
    while True:
        login(accounts)


main()
