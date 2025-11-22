# For programming we were tasked with making a questionear but after that the teacher wanted us to try and make something with a lot of oporators

# oprators to go through + - / * < > <= >= += -= == != 

# using + - / * 
# one of the easiers ways to do this is by using it in a calculator!

import time

"""""
num1 = int(input("Enter a number\n"))

todo = input("what functuion to use? (+ - / *)\n")

num2 = int(input("Enter a number\n"))

if todo == "+":
    total = num1 + num2
if todo == "-":
    total = num1 - num2
if todo == "/":
    total = num1 / num2
if todo == "*":
    total = num1 * num2
print(f"{num1}{todo}{num2} = {total}")

# < and > can be used to check for if something is greater or less than something else
# so it could be used give different answers depending on what the end users input is such as something like age

age = int(input("How old are you?\n"))
if age > 35:
    print("Damn how are you still able to walk or even read the question?")
if age < 35:
    print("Aww you're just a little baby!")
    
# for -= += you could use it in a game for example where your age would increase or your money would decrease

gameAge = int(input("How old do you want your ingame character to be?\n"))

print("After traveling from lands far away you stumble on a rock and break your leg and need to let it heal a few years pass...")
gameAge += 2
print(f"You are now {gameAge} years old and should concider if adventuring is something for you...")
"""
money = 4000
cow = 5000
pig = 4000
chicken = 3000
ani = input("you choose to retire and become a farmer instead!\n but every good farmer needs animals so which once do you want to buy? (cow/pig/chicken)")
if ani == "cow":
    money -= cow
    print(f"After spending all your lives savings on a single cow making you go {money} into debt you relize that you dont even have food for it...\nNo food, No money, No job...\n\n\n GAME OVER")
    exit()
    
if ani == "pig":
    money -= pig
    print(f"So you spend all your money on a single pig huh... you literaly have {money} coins left...\n So you decide to go into debt to try and make the farming life work for you!\nSadly the debt colectors are some shady people... shouldn't have borrowed from them i guess!\n\n\nYou make a living but nothing special... at least you didn't spend all your money on a single cow!")
    exit()
if ani == "chicken":
    money -= chicken
    print(f"after looking at the prizes for the other animals and seeing how expensive they are you decide to go with 15 chickens still leaving you with {money} coins left! plenty for food and some other small things you would need to keep them safe!")
    time.sleep(3)    
    print("A few years go by")
    time.sleep(3)
    print("That one guy who bought that crazy expensive cow died about a year ago and the other guy who bought the pig always has some shady people coming by...\nBest to not ask!")
    time.sleep(3)
    print("Meanwhile your chickens are laying thousands of eggs and money is flowing in!")    
    time.sleep(2)
    print("You already expanded your land, got a few workers, and plenty of more chickens!")
    time.sleep(3)
    print("30 Years later and you are the most welthy man in the contry!\nYour egg empire has expanded to lands far away!")
    time.sleep(2)
    print("Seems like chickens were the right choice back then!")
    time.sleep(3)
    print("GOOD ENDING")
    exit()
