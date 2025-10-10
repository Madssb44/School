# Advanced parking system task
 
# used to make running it feel more natural to how a program like this would work
from time import sleep

# Number of free spaces
spaces = 5

# List of license plates registered in the system
taken = []

# Loop to keep the program running
while True:
    # Basic menu screen with options
    print("""
          Welcome to the Parkingtower

--------------------------------------------------
If you want to park press                      (1)
If you want to get your parked car press       (2)
To see free spaces press                       (3)
To exit the program press                      (4)
--------------------------------------------------
""")
    what = input("Enter selection here: ")
    # if they pick 1 the program checks to see if theres space
    # If there isnt it sends them back to the welcome menu
    # if there is space it askes the user to enter their licence plate which it save to reg
        # it then checks to see if reg is already parked by checking if reg is in the list taken
        # if reg is in the list it sends the back to the welcome menu
        # if reg is not in the list it adds reg to the list and sets space to 1 less then sends you back to the welcome menu
    if what == "1":
        if spaces > 0:
            reg = input("Please enter your license plate here: ")
            if reg in taken:
                print("This lisance plate is already registered as parked in our system")
                sleep(2)
            elif reg not in taken:
                taken.append(reg)
                print("Registration succesful\nEnjoy your stay!")
                spaces -= 1
                sleep(2)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        elif spaces == 0:
            print("We are out of spaces at the moment come back later or wait for a free space")
            sleep(2)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # If they pick 2 the program prompts the user to enter their license place
        #If the input matches anything from the list taken it shows a goodbye message and removes the users input from the list and increses space by 1
        #If the input does not match anything from the list taken it sends them back to the welcome menu 
    if what == "2":
        print("Please enter your lisance plate: ")
        reg = input("")
        if reg in taken:
            print(f"""
       Thank you for chosing Parkingtower

---------------------------------------------------
{reg} is now unregistered

Payment process for {reg} = DONE

We hope to see you again!
---------------------------------------------------
""")
            taken.remove(reg)
            spaces += 1
            sleep(2)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        elif reg not in taken:
            print("There is no vehicle registered with this license plate.")
            sleep(2)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # If they pick 3 the program shows how many spaces there is left and then sends them back to the welcome menu
    if what == "3":
        print(f"There is {spaces} free spaces left")
        sleep(2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # If they pick 4 the program ends
    if what == "4":
        exit()
    