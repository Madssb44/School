# Making a calcualtor that will calcualte the avrage of the numbers you input


# def will define the text after 
# in this excample it will make div return a divided value of the information feed into the function
def div(x, y):
   return x / y 

# setting the starting value of total & count
# both are 0 since we have no data yet
total = 0
count = 0


# num = float(input("add a number: ")) 
# takes the number the user writes as a float
num = float(input("add a number: "))


# total += num
# adds num's value to total
total += num


# count += 1
# adds 1 to count  
count += 1 


# while True will loop the code making it be able to add more numbers without
# each new number requireing a new line of code
while True:
        # more will decide whats gonna happen in the loop
    more = input("Do you want to add another number? (yes/no) ")

        # if more == yes its gonna ask you to add a new number
    if more == "yes" or more == "y":
        num = float(input("add a number: "))
        total += num
        count += 1
        

        # if more == no its gonna give you the average of the information you have given it 
        # the break function ends the code
    if more == "no" or more == "n":
        average = div(total, count)
        print("Your total is ", total,"\nyour average is ", average)
        break

        # if neither is given its gonna go back to the begining of the loop
