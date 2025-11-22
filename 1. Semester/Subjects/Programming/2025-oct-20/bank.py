# Du skal lave et program, der simulerer en simpel bankkonto. Brugeren skal kunne:
# Se saldo
# Indsætte penge
# Hæve penge
# Afslutte programmet

# I skal skal bruge funktioner til at:
# Oprette en konto med en startsaldo
# Håndtere indbetalinger og hævninger
# Tjekke, om der er nok penge på kontoen før hævning
# Lave et simpelt menu-system
# Husk en main til at køre
from time import sleep

accounts = ["admin","test"]
passwords = ["admin","username"]
balances = [100000,350]

def startMenu():
   print("""
-----------------------------------------------------------------------------------         
                        Welcome to broke boy bank

You have the following options
                        
To login press 1
To create an account press 2   
to close the program press x

-----------------------------------------------------------------------------------
""")
   menu = input("")
   if menu == "x":
        exitProgram()
   elif menu == "1":
       login()
   elif menu == "2":
       creatAccount()

def loggedInMenu(account,password,balance):
    index = accounts.index(account)
    while True:
        
        print("""
    -----------------------------------------------------------------------------------
                            Welcome to broke boy bank

    You have the following options

    To see curent balance press 1
    To Deposite money press 2 
    To Withdraw money press 3        
    To Log out press x
            
    -----------------------------------------------------------------------------------   
            """)
        menu = input("")
        if menu == "x":
            return
        elif menu == "1":
            money = balances[index]
            print(f"You currently have {money}$ on your account")
            sleep(1)
        elif menu == "2":
            depositMoney(account=accounts[index])
        elif menu == "3":
            withdrawMoney(account=accounts[index])

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in accounts: # login check
            index = accounts.index(username)
            if password == passwords[index]:
                print("Login successful!")
                sleep(1)
                return loggedInMenu(account=accounts[index],password=passwords[index],balance=balances[index])
            else:
                print("Incorrect password")
                attempts -= 1
    print("Too many failed attempts. Exiting program.")
    sleep(1)
        
def showBalance(account):
    index = accounts.index(account)
    money = balances[index]
    print(f"You currently have {money}$ on your account")
    sleep(1) 

def depositMoney(account):
    index = accounts.index(account)
    amount = int(input("Enter the amount you want to deposit: "))
    balances[index] += amount
    print(f"Your new balance is {balances[index]}$")
    sleep(1)

def withdrawMoney(account):
    index = accounts.index(account)
    money = balances[index]
    amount = int (input("Enter the amount you want to withdraw: "))
    if money < amount:
        print("You don't have enough money to withdraw this amount")
        sleep(1)
    elif money >= amount:
        balances[index] -= amount
        print(f"Your new balance is {balances[index]}$")
        sleep(1)
        
def exitProgram():
    exit()

def creatAccount():
    username = input("Choose a username: ")     
    if username in accounts:
        print("username is already taken")
        sleep(1)
        creatAccount()
    password = input("Choose a password: ")
    accounts.append(username)
    passwords.append(password)
    balances.append(0)
    print("Account created successfully!")
    sleep(1) 
    return loggedInMenu(username,password,0)


def main():
    global accounts
    global passwords
    global balance
    while True:
        startMenu()
        
main()








# User = input("Choose a username: ")
# password = input("Choose a password: ")

# accounts.append(user)
# password.append(password)
# balance.append(0)

# return accounts, password, balance
 
