# Quiz with points task

# make a quiz with 5-10 questions keep track of points and sumorize in the end


import time
points = 0 
print("Welcome to the Old School Runescape quiz!")
time.sleep(2)
print("The questions will get harder and harder as you go on")
time.sleep(2)
q1 = input("What is the name of the you spawn into after tutorial island?\n1 = Varrock\n2 = Lumbridge\n3 = Falador\n")
if q1 == "2":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q2 = input("How many skills are there in osrs?\n1 = 18\n2 = 23\n3 = 25\n")
if q2 == "2":
    points += 1
    print("Corect!")
else: 
    print("Wrong")   
time.sleep(2)
q3 = input("In which city is the grandexchange?\n1 = Rimmington\n2 = Lumbridge\n3 = Varrock\n")
if q3 == "3":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q4 = input("How many inventroy stots do you have?\n1 = 24\n2 = 28\n3 = 32\n")
if q4 == "2":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q5 = input("Who do you have to deafeat to earn your firecape?\n1 = Jad\n2 = Zulrah\n3 = Yama\n")
if q5 == "1":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q6 = input("The game updates in ticks with each tick being how long?\n1 = 0.6 sec\n2 = 1 sec\n3 = 2.5 sec\n")
if q6 == "1":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q7 = input("Whats half of 99?\n1 = 44.5\n2 = 92\n3 = 98\n")
if q7 == "2":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q8 = input("What is the heighest combat level in the game?\n1 = 126\n2 = 702\n3 = 1563\n")
if q8 == "3":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q9 = input("Who is the the first person to earn the legendary infernocape?\n1 = Woox\n2 = Gnomemonkey\n3 = Odablock\n")
if q9 == "1":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)
q10 = input("When desert tresture 2 was released a fishing spot was found in stranglewood which holds the rarest drop in the game what is the drop rate?\n1 = 1/100,000\n2 = 1/ 250,000\n3 = 500,000\n")
if q10 == "3":
    points += 1
    print("Corect!")
else: 
    print("Wrong")
time.sleep(2)    
print("Time to see if you are a OSRS pro or not!")
time.sleep(2)
print(f"You got {points} points in total!")
time.sleep(2)

if points == 10:
    print("I think its time for you to touch some grass...")
    exit()
if points > 5:
    print("Seems like you know the game quite well! im glad to hear that!")
    exit()
if points > 2:
    print("looks like its about time you start playing!")
    exit()
if points == 0:
    print("Really... nothing... shame on you...")
    exit()