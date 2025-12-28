from time import sleep
import json
import os 

def masurement(log):
    try:
        temp = float(input('Enter the tempture you want to add: '))
        day = input('Enter the day you want it recorded to: ')
        saveToLog(day, temp, log)
    except TypeError:
        print('Invalid Input')
        sleep(2)
        masurement(log)


def loadLog():
    with open(f"{path}/log.json", "r", encoding="UTF-8") as f:
        log = json.load(f)
        return log

def saveToLog(day: str,temp: float, log):
    log[day] = [temp]
    writeToLog(log)
    more =  input('Do you want to add more?\n\n1. add more\n2. get statistics for current data\nq. get statistics for data and exit\n\n')
    while more not in('1','2','q'):
        print('Invalid Choice')
        more =  input('Do you want to add more?\n\n1. add more\n2. get statistics for current data\nq. get statistics for data and exit\n\n')

    if more == '1':
        masurement(log)
        
    if more == '2':
        showStats(log)
        sleep(2)
        masurement(log)

    if more == 'q':
        showStats(log)
        sleep(2)
        exit()


def writeToLog(log):
    path = os.path.abspath(path)
    with open(f"{path}/log.json", "w", encoding="UTF-8") as f:
        json.dump(log, f)

def showStats(log):
    count = 0
    total = 0

    for day in log.keys():
        days[day]
        for temp in day:
            count += 1
            total += temp

    averageTemp = total / count 


def main():
    log = loadLog()
    masurement(log)

main()
