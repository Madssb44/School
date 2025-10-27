from time import sleep

# setting  something to track the day and week
day = 0
week = 0

# awake state with options depending on if its the weekend, you just slept or are on your way to bed
def awake(state):
    global day
    if state == "slept":
        state = "awake"
        print("You got out of bed")
        sleep(0.1)
        return comute(state)

    if state == "weekend":
        state = "awake"
        print("Weekend over back to normal life")
        day = 0
        sleep(0.1)
        return comute(state)
    
    if state == "sleep":
        print("off to work you go!")
        state = "awake" 
        sleep(0.1)
        return comute(state)

# asleep state with checks to see if its gonna be the weekend and check for number of weeks and ending it on the 7th week
def asleep(state):
    global day
    global week
    if week == 7:
        print("The same thing over and over drives you crazy...")
        sleep(0.1)
        print("You die of no excitement in life")
        return None
    if day == 5:
        state = "weekend"
        print("you have a nice relaxing weekend!")
        week += 1
        sleep(0.1)
        return awake(state)
    if state == "ate":
        print("After a long day its off to sleep")
        state = "slept"
        day += 1
        sleep(0.1)
        return awake(state)
# at work state that checks if you have been on a break or not   
def atWork(state):
    if state == "work":
        state = "working"
        print("Time to get to work!")
        sleep(0.1)
        return onBreak(state)
    if state == "break":
        state = "finished"
        print("back from break off work soon!")
        sleep(0.1)
        return comute(state)
# commute state that checks if you are on your way to work or on your way home from work                
def comute(state):
    if state == "awake":
        state = "work"
        print("You take the train to work")
        sleep(0.1)
        return atWork(state)
    
    if state == "finished":
        state = "home"
        print("after work you take the train home")
        sleep(0.1)
        return cooking(state)
    
# cooking because food is important! 
def cooking(state):
    state = "ate"
    print("Home from work time to cook!")
    sleep(0.1)
    return asleep(state)

# breaks are important! so better take your daily break!
def onBreak(state):
    state = "break"
    print("You take your daily break")
    sleep(0.1)
    return atWork(state)

# Setting the first stage and starting the code
state = "sleep"
life = awake
while life:
    life = life(state)
