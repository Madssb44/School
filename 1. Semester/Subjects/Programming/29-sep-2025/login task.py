# Making a loginsystem 

username = ["admin","user","broke"]
password = ["admin","userpass","brokepass"]

admin = 0
user = 0 

while True:
    uu_att = 3
    while uu_att > 0:
        todo = input("What do want to do?\n1 = Login\n2 = Register a new user\n")
        if todo =="1":
            uu = input("Enter username: ")
            if uu == username[0]:
                print("Corect username")
                break
            if uu in username[1:]:
                print("Corect username")
                break
            else:
                uu_att = uu_att - 1
                print("Username does not exist, attempts remaining ", uu_att)
            if uu_att == 0:
                print("failed to enter active username")
                exit()
        if todo =="2":
            newuser = input("Enter the username you want to register as: ")
            newpass = input("Enter the password: ")
            username.append(newuser)
            password.append(newpass)
            todo = 0

 
    up_att = 3
    while up_att > 0:
        up = input("Enter password: ")
        if up == password[0]:
            print("Corect passowrd")
            admin = 1 
            break
        if up in password[1:]:
            print("Corect password")
            user = 1 
            break
        else:
            up_att = up_att - 1
            print("Incorect password, attempts remaining: ", up_att)
        if up_att == 0:
            print("Failed to enter corect password!")
            exit()
    
    if admin == 1:        
        while admin == 1:
            print("You are logged in as a admin")
            todoadmin = input("What do you want to do?\n1 = Remove a user\n2 = Log out\n")
            if todoadmin == "1":
                print(username[1:])
                remove = input("Who do you want to remove?\n type the name of the user you want to remove\n")
                indexuser = username.index(remove)
                username.remove(remove)
                password.remove(password[indexuser])
                todoadmin = 0
            if todoadmin == "2":
                print("Have a wonderful day!")
                break
    if user == 1:
        while user == 1:
            print("You are logged in as a user")
            todouser = input("What do you want to do?\n1 = Remove a user\n2 = Log out")
            if todouser == "1":
                print("You don't have credintials to do that")
            if todouser == "2":
                print("Have a nice day!")
                user = 0
    else:
        continue
        
