# I har fået listen Liste: [10, 4, 6, 2, 8]

# Jeg vil gerne have et program der kan finde summen, det næst største tal og gennemsnittet.

# i må ikke bruge sort(), max() eller sum() fra liste.

# The things i use for my loop to get the average, total and amount of numbers on the list
amount = 0
index = -1
total = 0
numbers = [10, 4, 6, 2, 8]

# The things i use to get the second heighest number
b = 0
sb = 0

# to get the average

for i in numbers:
    amount += 1
    index += 1
    numb = numbers[index]
    total += numb
    average = total / amount

for i in numbers:   
    if i > b:
        b = i
    elif i < b and i > sb:
        sb = i
    elif i < sb:
        continue 
    


print(f"And the second heighest number is {sb}")
print(f"The total sum of all your numbers is {total} you have a total of {amount} numbers the average is {average}")
