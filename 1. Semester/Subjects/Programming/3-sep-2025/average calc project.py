def div(x, y):
    return x / y 
def average_calc():
    count = 0
    total = 0
    amount_to_calc = int(input("how many grades do you want to average out: "))
    while amount_to_calc > 0:
        num = int(input("Enter a grade: "))
        total = total + num
        count = count + 1
        amount_to_calc = amount_to_calc - 1
    print("The average of your grades is: ", div(total, count))    
average_calc()

    

