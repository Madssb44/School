#
# Welcome DONE
# if stats DONE
##################
# is user DONE
# average age DONE
# find my ticket DONE
# exit to welcome DONE
##################
# is admin DONE
# find ticket DONE
# average age DONE
# list of people DONE
# exit to welcome DONE
##################
# if get ticket DONE
# get name DONE
# get age DONE
# check age DONE
# if too young DONE
# Check for parent in find ticket DONE
# attach parent to data DONE

# get type DONE
# save data on list DONE
# print data DONE
# exit to welcome DONE

# Price pr ticket
# depending on ticket type
# active events stored in directories with nameofevent and fullentryofevent
# Admin that can make/remove events
# when getting a ticket you can attend a event
# nameofevent for printing list of events
# fullentroyofevent for detailed information on the event

from time import sleep

username = "admin"
password = "admin"

ageOfAll = 0
allTimeUsers = 0

nameOfCustomer = ["Mads Buhl", "Mads Mikkelsen"]
ageOfCustomer = ["26", "56"]
typeOfTicket = ["student", "VIP"]
eventNameList = []
fullEventEntryList = []


def clear():
    print("\n" * 100)


def welcomeMenu():
    print("""
##########################################################################################
Welcome to the not personal data stealing ticket center

If you want to order a ticket press 1
If you want to review statistics that totally aren't personal information press 2

##########################################################################################""")
    goTo = input("Enter your choice: ")
    if goTo == "1":
        getTicket()
    if goTo == "2":
        toStats()


def toStats():
    clear()
    print("""
##########################################################################################

If you want to get information on your own ticket press 1
If you want to see the average age of people who use this site press 2
If you want to access the admin dashboard press 3

##########################################################################################""")
    goTo = input("Enter your choice: ")
    if goTo == "1":
        getPersonsInformation()
    if goTo == "2":
        print("Getting average!")
        sleep(1)
        averageAge()
    if goTo == "3":
        print("Sending to login page!")
        sleep(1)
        login()


def login():
    clear()
    attempts = 3
    while attempts > 0:
        user = input("Enter username: ")
        passwd = input("Enter password: ")
        if user == username:
            if passwd == password:
                print("Access granted!")
                adminDashboard()
        else:
            print("Wrong username or password")
            attempts -= 1


def adminDashboard():
    while True:
        clear()
        print("""
    ##########################################################################################
    Welcome to the admin dashboard

    to view average age press 1
    to find a ticket from a name press 2
    to print a list of all ordered tickets press 3
    to make a new event press 4
    to remove a event from active events press 5
    to exit admin dashboard press q
    ##########################################################################################""")

        goTo = input("Enter your choice: ")
        if goTo == "1":
            print("Getting average")
            sleep(1)
            averageAge()
        if goTo == "2":
            getPersonsInformation()
        if goTo == "3":
            printList()
        if goTo == "4":
            makeEvent()
        if goTo == "5":
            removeEvent()
        if goTo == "q":
            welcomeMenu()


def makeEvent():
    clear()
    eventName = input("Enter the name of the event you wish to create: ")
    while eventName in eventNameList:
        eventName = input(
            "Theres already a event with that name.\nEnter new name here: "
        )
    eventDate = input("Enter the date the event will be held: ")
    eventPrice = input(
        "Enter the prise a standard ticket will cost\nThe price needs to be a whole number!\nEnter price here: "
    )
    while eventPrice:
        check = eventPrice.isdigit()
        if check:
            break
        else:
            print(
                "Invalid input...\nNumber must be a whole number\nNo use of letters or special characters allowed\n"
            )
            sleep(1)
            eventPrice = input("Enter price here: ")

    eventVIPAndStudentPrise = input(
        "Do you want to set prises for VIP and student tickets or use the standard formula?\nTo set prises manually press 1\nTo use standard formula press 2\n"
    )
    while eventVIPAndStudentPrise not in ("1", "2"):
        eventVIPAndStudentPrise = input("Invalid option please enter valid input: ")
    if eventVIPAndStudentPrise == "1":
        standardTicketPrice = eventPrice
        VIPTicketPrise = input("Enter the prise for a VIP ticket: ")
        while VIPTicketPrise:
            check = VIPTicketPrise.isdigit()
            if check:
                break
            else:
                print(
                    "Invalid input...\nNumber must be a whole number\nNo use of letters or special characters allowed\n"
                )
                sleep(1)
                VIPTicketPrise = input("Enter price here: ")

        studentTicketPrice = input("Enter the prise for a student ticket: ")
        while studentTicketPrice:
            check = studentTicketPrice.isdigit()
            if check:
                break
            else:
                print(
                    "Invalid input...\nNumber must be a whole number\nNo use of letters or special characters allowed\n"
                )
                sleep(1)
                studentTicketPrice = input("Enter price here: ")

    elif eventVIPAndStudentPrise == "2":
        standardTicketPrice = eventPrice
        VIPTicketPrise = str(int(eventPrice) * 1.3)
        studentTicketPrice = str(int(eventPrice) * 0.8)
    shortDescriptionOfEvent = input("Write a short description of the event: ")
    fullEventEntry = (
        "Event name: "
        + eventName
        + "\nThe event will be held the: "
        + eventDate
        + "\nPrices for tickets:\nStandard ticket prise: "
        + standardTicketPrice
        + "DKK\nVIP ticket price: "
        + VIPTicketPrise
        + "DKK\nStudent ticket price: "
        + studentTicketPrice
        + "DKK\n\n\nShort description of the event:\n\n"
        + shortDescriptionOfEvent
        + "\n\n\n"
    )
    eventNameList.append(eventName)
    fullEventEntryList.append(fullEventEntry)
    print(
        f"The following has been added as a event to the list of active events: {eventName}\nDetailed view:\n{fullEventEntry}"
    )
    input("Press enter to return to")


def removeEvent():
    if eventNameList:
        print("The current active events are listed below")
        for event in eventNameList:
            print(event)
        whatToRemove = input(
            "Enter the name of the event you want to remove\nYour input is case sensitive so make sure you spell it right\nEnter the name here: "
        )
        while whatToRemove:
            if whatToRemove in eventNameList:
                index = eventNameList.index(whatToRemove)
                del eventNameList[index]
                del fullEventEntryList[index]
                print(f"{whatToRemove} has been removed from active events")
                more = input("Do you want to remove more?\nYes\nNo\n")
                if more not in ("Yes", "No", "yes", "no"):
                    while more:
                        more = input(
                            "invalid input...\n\nDo you want to remove more?\nYes\nNo\n"
                        )
                        if more not in ("Yes", "No", "yes", "no"):
                            continue
                        else:
                            break
                elif more in ("yes", "Yes"):
                    removeEvent()
                elif more in ("no", "No"):
                    adminDashboard()

            else:
                print(
                    f"{whatToRemove} was not found in the list of active events\nMake sure you spelled it right\n"
                )
                whatToRemove = input(
                    "Enter the name of the event you want to remove or type 'list' to print the active events again\n"
                )
                if whatToRemove == "list":
                    for event in eventNameList:
                        print(event)
                    whatToRemove = input(
                        "Enter the name of the event you want to remove: "
                    )
    else:
        print("Theres no active events at the moment...")
        sleep(1)


def averageAge():
    global allTimeUsers
    global ageOfAll
    average = ageOfAll / allTimeUsers
    print(f"the average age of all customers is {int(average)} years")


def printList():
    print("Generating list...")
    sleep(1)
    nr = 0
    for person in nameOfCustomer:
        index = nameOfCustomer.index(person)
        nameToPrint = nameOfCustomer[index]
        ageToPrint = ageOfCustomer[index]
        ticketTypeToPrint = typeOfTicket[index]
        personNr = "Customer nr: " + str(nr)
        printable = (
            personNr
            + " Name: "
            + nameToPrint
            + " "
            + "Age: "
            + str(ageToPrint)
            + " Ticket type: "
            + ticketTypeToPrint
        )
        print(printable)
        nr += 1
    input("When you are done reading the list press enter to return to dashboard")


def getPersonsInformation():
    clear()
    print(
        "You need to enter the first and last name of the ticket you want information for\nIf more than 1 person exists with the name more information will be needed\n"
    )
    sleep(1)
    firstName = input("Enter the owners first name: ")
    lastName = input("Enter the owners last name: ")
    fullName = firstName + " " + lastName
    matches = 0
    for name in nameOfCustomer:
        if fullName in nameOfCustomer:
            if name == fullName:
                matches += 1

    if matches == 1:
        index = nameOfCustomer.index(fullName)
        nameToPrint = nameOfCustomer[index]
        ageToPrint = ageOfCustomer[index]
        ticketTypeToPrint = typeOfTicket[index]
        printable = (
            "Information for the ticket:\n\nName of the owner: "
            + nameToPrint
            + "\nAge of the owner: "
            + str(ageToPrint)
            + "\nType of ticket: "
            + ticketTypeToPrint
            + "\n\nTo return to welcome page press enter"
        )
        print(printable)
        input("")

    elif matches > 1:
        print("Additional information required")
        age = input("Enter the owners age: ")
        for person in ageOfCustomer:
            if age in ageOfCustomer:
                ageIndex = ageOfCustomer.index(age)
                nameIndex = nameOfCustomer.index(fullName)
                if ageIndex == nameIndex:
                    nameToPrint = fullName
                    ageToPrint = age
                    ticketTypeToPrint = typeOfTicket[ageIndex]

                    printable = (
                        "Information for the ticket:\n\nName of the owner: "
                        + nameToPrint
                        + "\nAge of the owner: "
                        + str(ageToPrint)
                        + "\nType of ticket: "
                        + ticketTypeToPrint
                        + "\n\nTo return to welcome page press enter"
                    )
                    print(printable)
                    input("")
                    break

    elif matches == 0:
        print(
            "No ticket found with the provided name\nYou will be sent to the welcome page shortly"
        )
        sleep(2)


def getTicket():
    global allTimeUsers
    global ageOfAll
    clear()
    print(
        "##########################################################################################"
    )
    print("Welcome to the registration page!\n")
    print("""
You will need to provide your: 
First name
Last name
age
type of ticket

if theres a ticket with your information in the system already you wont be able to register for another one\n\n
##########################################################################################""")
    sleep(2)
    while True:
        firstName = input("Enter your first name: ")
        lastName = input("Enter your first name: ")
        age = input("Enter your age: ")
        if int(age) <= 15:
            print(
                "You are too young to go by yourself so you need a parent to accompany you\nYour parent needs to have a ticket registered before you can order one"
            )
            parent = input(
                "Does your parent have a ticket?\nIf your parent has a ticket press 1\nIf your parent doesn't have a ticket press 2\n"
            )
            if parent == "1":
                print(
                    "You need to enter the information registered on your parents ticket"
                )
                parentFirstNameCheck = input("Enter their first name: ")
                parentLastNameCheck = input("Enter their last name: ")
                parentAgeCheck = input("Enter their age: ")
                parentTicketTypeCheck = input("Enter their ticket type: ")
                parentsFullNameCheck = parentFirstNameCheck + " " + parentLastNameCheck
                if parentsFullNameCheck in nameOfCustomer:
                    index = nameOfCustomer.index(parentsFullNameCheck)
                    if parentAgeCheck == ageOfCustomer[index]:
                        if parentTicketTypeCheck == typeOfTicket[index]:
                            print("The information matches with a existing ticket!")
                        else:
                            print("The information doesn't match a existing ticket")
                            break
                    else:
                        print("The information doesn't match a existing ticket")
                        break
                else:
                    print("The name doesn't match any existing tickets")
                    break
            if parent == "2":
                break
        ticketType = input(
            "What type of ticket do you want to order?\nIf you want a standard ticket press 1\nIf you want a VIP ticket press 2\nIf you want a student ticket press 3\n\n"
        )
        if ticketType == "1":
            ticketType = "standard"
        if ticketType == "2":
            ticketType = "VIP for a wonderful person like yourself"
        if ticketType == "3":
            ticketType = "student"
        fullName = firstName + " " + lastName
        if fullName in nameOfCustomer:
            index = nameOfCustomer.index(fullName)
            if age == ageOfCustomer[index]:
                print("There is already a ticket registered with this information")
                sleep(1)
                break
            elif age != ageOfCustomer[index]:
                nameOfCustomer.append(fullName)
                ageOfCustomer.append(age)
                typeOfTicket.append(ticketType)
                ageOfAll += int(age)
                allTimeUsers += 1
                sleep(1)
                print("ticket information: ")
                printable = (
                    "\n\nTicket for: "
                    + fullName
                    + "\nAge: "
                    + age
                    + "\nTicket type: "
                    + ticketType
                )
                print(printable)
                break
        elif fullName not in nameOfCustomer:
            nameOfCustomer.append(fullName)
            ageOfCustomer.append(age)
            typeOfTicket.append(ticketType)
            ageOfAll += int(age)
            allTimeUsers += 1
            sleep(1)
            print("Ticket information: ")
            printable = (
                "\n\nTicket for: "
                + fullName
                + "\nAge: "
                + age
                + "\nTicket type: "
                + ticketType
            )
            print(printable)
            break


def main():
    global ageOfAll
    global allTimeUsers
    global nameOfCustomer
    global ageOfCustomer
    global typeOfTicket
    global username
    global password
    while True:
        welcomeMenu()


main()
