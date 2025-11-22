# Lav en funktion der tager 3 parameter.
# Med de parameter skal den finde gennemsnittet af værdien og printe resultatet.

# Husk at kalde funktionen til sidst.
def calc():
    total = 0
    ammount = 0
    while True:
        numb = input("Enter your value as a number\nType 'done' when you are finished: ")
        if numb == 'done':
            average = total / ammount
            print(f"Your average is : {average}")
            break
            
        if numb != 'done': 
            numb = float(numb)
            total += numb
            ammount += 1


def main():
    while True:
        calc()

main()
