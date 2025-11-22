# Making a parking 

# We need spaces and a menu for if you arent parked yet

# we need a menu for when you are parked
spaces = 5


print("Welcome to the parkingtower") 
while spaces>0:
    menu1 = input("What do you want to?\n1 = see how many spaces are free\n2 = Book a parking spot\n3 = Exit the program\n")
    if menu1 == "1":
        print(f"There are {spaces} free spots")
        menu1 = 1
    if menu1 == "2":
        print("Perfect! your spot is a5")
        spot = "a5"
        spaces -= 1
        while spot == "a5":
            menu2 = input("Anything we can help with?\n1 = I want to leave\n2 = how many spots are left?")
            if menu2 =="1":
                print("Alright i hope you had a wonderful expeirance being parked here!")
                spaces += 1
                spot = 0
            if menu2 =="2":
                print(f"There is {spaces} parking spots left")
    
    if menu1 == "3":
        print("We hope to see you again!")
        exit()
    
            
