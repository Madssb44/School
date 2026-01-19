def login(usersn, usersp, att):
    if att == 0:
        print("You have used too many attempts closing program!")
        exit()

    if not usersn:
        createACC(usersn, usersp)
 
    user = input("Enter username: ")
    passwd = input("Enter password: ")
    check(user, passwd, usersn, usersp, att)    

def createACC(usersn, usersp):
    username = input("Enter username")
    passwd = input("Enter password")
    
    usersn.append(username)
    usersp.append(passwd)


def check(name,passwd, usersn, usersp, att):
    if name in usersn:
        index = usersn.index(name)
        if passwd in usersp[index]:
            userMenu(name)
    if name == "admin":
        if passwd == "admin":
            adminMenu()
    else: 
        att -= 1
        print("Username or password was wrong try again!")


def adminMenu():
    spaces = 9999
    while True:    
        print("Welcome to the admin dashboard!")
        choice = input("\n\nto see orders press 'o'\nto see spaces left press 's'\nto return to loging press 'x'")

        if choice == "o":
            print("hello")
        if choice == "s":
            print(f"Theres too {spaces} spaces left!")

        if choice == "x":
            return   
def userMenu(name):
    print(f"Welcome {name}\n the current avaliable types of tickets are: \n\nStandard ticket for 350 Dkk\nVIP ticket for 700 Dkk\n\nPress x to go to cart")
    totalprize = 0
    while True:
        choice = input("Enter the type of ticket you want to buy:\ns[standard]\nv[ip]\ne[x]it")
        if choice == "s":
            amm = int(input("Enter the amount of tickets to buy: "))
            totalprize += calcstandard(amm)
        if choice == "v":
            amm = int(input("Enter the amount of tickets to buy: "))
            totalprize += calcvip(amm)
        if choice == "x":
            ordername.append(name)
            orders.append(int(totalprize))
            printDone(totalprize)

def calcstandard(amm):
    totalprize = amm * 350
    return totalprize

def calcvip(amm):
    totalprize = amm * 700
    return totalprize

def printDone(totalprize)
    print(f"Your total is {totalprize}")
    input("Press enter to continue")

def main():
    usersn = []
    usersp = []
    att = 3
    ordername = []
    orders = []
    login(usersn, usersp, att)

while True:
    main()
