# Du skal lave et program, der registrerer studerende til et kursus. Det skal laves med funktioner. 
# Tænk på en funktion til hvad programmet skal kunne

# Programmet skal:

# Lade brugeren tilføje studerende til en liste.
# Lade brugeren fjerne studerende og gerne mere end en af gangen.
# Udskrive den fulde liste, når de er færdige.

# I skal tænke over:

# Hvordan kan i bruge en liste til at gemme studerende?
# Hvordan kan i bruge loops og if-statements til at styre input?
# Hvordan kan i bruge funktioner til at holde koden struktureret?
# Husk jeres strip funktion

# Ekstra vis man har lyst
# I skal kunne registrer underviser og lokaler til undervisning. 

# Så kan en underviser se hvilke studerende der er i en klasse.
from time import sleep

students = ["hansejner","bob","bo","andy","harold","bobby","bobiline","leif","ejner","gertrud","åse","ragnhild"]
rooms = ["eaaa","aarhus univeresity","online"]
teachers = ["Philip","Kasper","Lasse"]
takenRooms = []
courses = []
def menu():
    print("#"* 64)
    print("# Welcome to Super Duper Smart School")
    print("#")
    print("#")
    print("# To add students press 1")
    print("# To remove students press 2")
    print("# To make a course press 3")
    print("# To add students to a course press 4")
    print("#")
    print("# To close the program press x")
    print("#")
    print("#" * 64)
    menuInput = input("")
    if menuInput == "1":
        return addStudents()
    if menuInput == "2":
        return removeStudents
    if menuInput == "3":
        
    if menuInput == "4":
    if menuInput == "x":
        exit()



def addStudents():
    print("Enter the first name of the students you want to add to the list of students\nIf you want to add more than one enter a , in betweet each name:\n")
    names = input("").lower()
    toAdd = names.split(",")
    for name in toAdd:
        students.append(name)
        print(f"{name} has been added to the list of students")
        sleep(0.5)
        
def removeStudents():
    print("Enter the first name of the students you want to remove from the list of students\nIf you want to remove more than one enter a , between name:\n")
    names = input("").lower()
    toRemove = names.split(",")
    for name in toRemove:
        students.pop(name)
        print(f"{name} have been removed")
        sleep(0.5)    

def bookClass():
    name = input("What is the name of the course you want to make: ").title()
    
    subject = input("Whats the subject you will be teaching about: ").title()
    
    where = input("Where will the course be held: ").lower()
    
    teacher = input("Who will be teaching the course: ")
    
    
def main():
    menu()
    
    
main()