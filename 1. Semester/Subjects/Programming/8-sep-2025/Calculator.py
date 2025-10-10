# making a calcualtor 


# this funtion adds 2 numbers together
def add(x, y):
    return x + y

# This funtion subtracts 2 numbers from eachother
def subt(x, y):
    return x - y

# This funtion multiplies 2 numbers together
def mult(x, y):
    return x * y

# This function devides 2 numbers with each other
def div(x, y):
    return x / y


print("lets get started...")

while True:

    num1 = float(input("enter first number: "))
    Choice = input("what do you want do?\nadd\nsubt\nmult\ndiv\n-----\n")
    num2 = float(input("enter second number: "))

    if Choice in ('add', 'subt', 'mult', 'div'):
        if Choice == 'add':
             print(num1, "+", num2, "=", add(num1, num2))

        elif Choice == 'subt':
            print(num1, "-", num2, "=", subt(num1, num2))
    
        elif Choice == 'mult':
            print(num1, "*", num2, "=", mult(num1, num2))
    
        elif Choice == 'div':
            print(num1, "/", num2, "=", div(num1, num2))

        next_calcualtion = input("Lets's do the next calcualtion? (yes/no): ")
        if next_calcualtion == "no":
           break
    
    else:
        print("Invalid Input")
