# step counter advent project!

def addWeek(weeks: dict, count: int) -> tuple[dict, str, int]:
    weekdays = {"Monday": 0,
            "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0 } 
    test = "Week " + str(count) 
    if test in weeks.keys(): 
        count += 1 
        week = "Week " + str(count) 
        weeks[week] = weekdays 
        print(weeks) 
        steps(weeks, week, count) 
    else:
        week = "Week " + str(count)
        weeks[week] = weekdays
        print(weeks)
        steps(weeks, week, count)
            
def steps(weeks: dict, week: str, count: int) -> dict | int:
    for day, step in weeks[week].items():
        if step == 0:
            print(f"Currently registering steps for {week}, {day}\n\n")
            amount = input("How many steps did you walk today: ")
            weeks[week][day] = amount
    more(weeks, count)
    
def more(weeks: dict, count: int) -> dict | int:
    print("You are now done registering for the week!")
    match input("Do you want to add another week?\n1 = yes\n2 = no\n"):
        case "1":
            addWeek(weeks, count)
        case "2":
            showStats(weeks)
                    
def showStats(weeks: dict):
    total = 0
    average = 0
    max = 0
    weeknum = 0
    for week in weeks.values():
        weeknum += 1
        for day, steps in week.items():
            average += 1
            total += int(steps)
            if int(steps) > max:
                max = int(steps)
                printableMax = f"The day with the most steps was {day} in week {weeknum} with {steps}!"
                average = total / average
    
    print(f"The average of your registered steps are: {round(average, 2)} steps!\n{printableMax}\nKeep up the good work!\n\nUntil next time!")
    exit() 

def main():
    weeks = {}
    count = 1
    while True:
        print("Starting step counter!")
        addWeek(weeks, count)
        
main()

