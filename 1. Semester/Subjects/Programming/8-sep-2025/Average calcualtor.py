#project file for making a avrage calculator


# Creat a list
total = [36, 91, 46, 66]
# you can add things to the list to start with by putting it in the []
# Fx total = [29, 89, 36]


# add the numbers to the list
total.append(21)
# you can add both stings, floats, intidgers and variables to a list


# add more than one thing to a list
total.extend([11, 21])


# Finding the total and the average
# sumOfhumbers will become the total amount and starts at zero1
# count will be the number of times a number has been added to sumOfnumbers starts at zero


# for number in total: When a number occures in total the code under happends
# sumOfnumbers += number: will add number to sumOfnumber
# Count += 1

sumOfnumbers = 0
count = 0 
for number in total: 
    sumOfnumbers +=  number
    count += 1


# to find the avrage you need to divide the sumOfnumbers by count
# or the total amount by the number of times a number have been added
average = sumOfnumbers / count

print("the list of numbers is:", total)
print("the average of all the numbers is:", average)
