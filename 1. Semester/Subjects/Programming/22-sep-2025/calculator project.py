#tasked to make a calculator 

n1 = float(input("Enter a number: "))
fun = 1
while fun > 0:
    function = input("Choose a function: + - * /\n\n")
    if function == "+":
        n2 = float(input("Enter the second number: "))
        total = n1 + n2
        break
    if function == "-":
        n2 = float(input("Enter a number: "))
        total = n1 - n2
        break
    if function == "*":
        n2 = float(input("Enter a number: "))
        total = n1 * n2
        break
    if function == "/":    
        n2 = float(input("Enter a number: "))
        total = n1 / n2
        break
    else:
        print("Wrong input use a supported function!")
        
print(f"{n1} {function} {n2} = {total}")


# I am writing this to fill out the file to be over 1 KB beacuse if its smaller it can't be uploaded to canvas and will cause me to not be able to send it over :D 