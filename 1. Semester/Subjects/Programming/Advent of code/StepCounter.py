def addWeek(weeks: dict, count: int) -> dict | str | int:
    weekdays = {"Monday": 0,
            "Tuesday": 0,
            "Wednesday": 0,
            "Thursday": 0,
            "Friday": 0,
            "Saturday": 0,
            "Sunday": 0
    }
    
    test = "week " + str(count)
    
    if test in weeks:
        count += 1
        week = "Week " + count
        weeks[week:weekdays]
        steps(weeks, week, count)
    else:
        week = "Week " + count
        weeks[week:weekdays]
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
            exit()
            
def main():
    weeks = {}
    count = 1
    while True:
        addWeek(weeks, count)