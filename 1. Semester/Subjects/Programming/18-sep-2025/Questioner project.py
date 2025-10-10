# Todays task is to make a questioner 

import time

print("Hello nice to meet you! i have questioner for you i hope you would like to answer it!")

time.sleep(1)

answer = input("Do you want to answer the questions? (yes/no)\n")

time.sleep(1)

if answer == "yes".lower:
    name = input("Whats your name?\n")

    print(f"Hello there {name} nice to meet you!")

    time.sleep(2)

    year = int(input("What year were you born in? if you dont mind of course!\n"))

    yet = input("Have you had your birthday this year? (yes/no)\n")
    if yet == "yes": 
        age = 2025 - year
    else:
        age = 2024 - year

    print(f"Oh you young buck! only {age} years old")

    time.sleep(2)

    home = input("Do you live in either: aarhus, viby or silkeborg? (yes/no)\n")
    if home == "yes":
        city = input("Alright which one? (aarhus, viby or silkeborg)\n")
        if city == "aarhus":
            km = int(input("Ohh nice how many km do you have to EAA?\n"))
        if city == "viby":
            km = int(input("ahh nice and close! how many km do you have to EAA then?\n"))
        if city == "silkeborg":
            km = int(input("Oh thats quite far away! how many km is that form EAA?\n"))
    if home == "no":
        city = input("Okay which city do you live in then?\n")
        print(f"Alright i dont think i know where {city} is how many km is it away from EAA?\n")
        km = int(input())

    print(f"alright so you live in {city} and have {km}km to get to EAA!")

    time.sleep(1)

    if km > 20:
        print("Wow thats quite a distance you must have a long commute!\nBut plenty of time to relax on the way home!")
    if km < 20:
        print("Ohh nice you must have a short commute then!")

    time.sleep(2)

    color = input("Well heres a different question! whats your favorite color?\n")

    print(f"Ahh wonderful i love {color} as well!")

    time.sleep(2)

    food = input("Whats your favorite meal?\n")

    print(f"Ohh sounds nice i don't think i have had {food} before!")

    time.sleep(2)

    fact = input("alright the last question! tell me a fun fack about yourself!\n")

    print("ahh i interesting! thats a fun fact!")

    time.sleep(2) 

    print(f"Alright so to summarize it all!\nYour name is {name}, you live in {city} which is {km}km away from EAA!")

    time.sleep(1)

    print("lovely name by the way!")

    time.sleep(2) 

    print(f"You are {age} years old and look great for your age!")

    time.sleep(2)

    print(f"Your favorite color is {color}! such a pretty color!")

    time.sleep(2)

    print(f"Your favorite meal is {food} and you have to make it for me sometime so i can try it as well!")

    time.sleep(2)

    print(f"And my favorite part a fun fact about yourself is:\n{fact}")

    time.sleep(2)

    print("Thank you so much for answering i hope you had fun!")
    
    print("Your soul is signed away now btw hope you don't mind!")
    
if answer == "no":
    print("Ohh alright then i hope you have a great day!")
    exit()
