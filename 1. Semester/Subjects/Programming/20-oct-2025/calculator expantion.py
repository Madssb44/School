# Jeg vil gerne have i opgraderer jeres lommeregner kode. Tænk på vist eksempel.

# Lommeregner vil jeg gerne have i laver en funktion der hedder calculate.
# Den skal tage parameter som er to tal og en operator.

# calculate returner så udregningen

# Lav en funktion kaldet tjekForQ. Den tager en parameter som er en string. 
# Den skal returne True eller False.

# Lav en funktion kaldet Main() den skal være void(ingen parameter eller return) 
# Den skal køre koden og kalde de andre funktioner.

def checkforQ(q):
    if q == "q":
        exit() 
    
def calculate(n1, n2, fun):
    if fun == "+":
        print(f"{n1} + {n2} = {n1 + n2}")
    elif fun == "-":
        print(f"{n1} - {n2} = {n1 - n2}")
    elif fun == "*":
        print(f"{n1} * {n2} = {n1 * n2}")
    elif fun == "/":
        print(f"{n1} / {n2} = {n1 / n2}")
    elif fun != "+" or "-" or "*" or "/":
        print("Wrong input use a supported function!")

def main():
    while True:
        q = input("If you want to quit the program press 'q' to continue press enter: ")
        checkforQ(q)
        n1 = float(input("Enter a number: "))
        fun = input("Enter the function you want to use: + - * /\n ")
        n2 = float(input("Enter the second number: "))
        calculate(n1, n2, fun)

main()

