from time import sleep

def mainMenu(trainPrice: int, carPrice: float):
    print(f"Transport Comparison app!\n\nCurrent price for train trip = {trainPrice} DKK\nCurrent price for car trip = {carPrice} DKK\n\n\n1. See price for train ride\n2. See price for car ride\n3. Reset price to 0\nq. exit program\n")
    match input():
        case "1":
            trainCalc(trainPrice, carPrice)
        case "2":
            carCalc(trainPrice, carPrice)
        case "3":
            trainPrice = 0
            carPrice = 0
            mainMenu(trainPrice, carPrice)
        case "q":
            exit()
        case _:
            print("\n\n\nInvalid input\n\n\n")
            sleep(2)
            mainMenu(trainPrice, carPrice)


def trainCalc(trainPrice: int, carPrice: float):
    try:
        distance = int(input("Enter the number of zones you are going: "))
        newTrainPrice = distance * 12 + trainPrice
        mainMenu(newTrainPrice, carPrice)
    
    except TypeError:
        print("\n\n\nInvalid input\n\n\n")
        sleep(2)
        trainCalc(trainPrice, carPrice)
        

def carCalc(trainPrice: int, carPrice: float):
    try:
        distance = float(input("Enter the amount of km you are travling: "))     
        newCarPrice = distance * 23 + carPrice
        mainMenu(trainPrice, newCarPrice)
    
    except TypeError:
        print("\n\n\nInvalid input\n\n\n")
        sleep(2)
        carCalc(trainPrice, carPrice)


def main():
    while True:
        mainMenu(0,0)


main()
