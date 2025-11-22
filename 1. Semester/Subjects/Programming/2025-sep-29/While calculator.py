# making a calculator
done = 0

while done != 1:
    fun = input("Enter the function you want to use: + - * / % ")
    n1 = float(input("Enter a number: "))
    if fun == "+":
        n2 = float(input("Enter the second number: "))
        total = n1 + n2
        break
    if fun == "-":
        n2 = float(input("Enter a number: "))
        total = n1 - n2
        break
    if fun == "*":
        n2 = float(input("Enter the second number: "))
        total = n1 * n2
        break
    if fun == "/":    
        n2 = float(input("Enter the second number: "))
        if n2 == 0:
            print("You know you cant do that...")
        if n2 != 0:
            total = n1 / n2
            break
    if fun =="%":
        n2 = float(input("Enter the second number: "))
        total = n1 * n2 / 100
        break
    else:
        print("Wrong input use a supported function!")
        
print(f"{n1} {fun} {n2} = {total}")
