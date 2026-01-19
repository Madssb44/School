from time import sleep

def order(orderNR: int):
    orderList = {}
    water = 10 
    beer = 20 
    Drinks = 30 

    addOrder = input("Do you want to add a new order?\ny[es] i want to add a new order!\nn[o] im done for today!")
    if addOrder == "y":
        orders = []
        while True:
            print("Items to pick from!\n\nw[ater] = 10 Dkk\nb[eer] = 20 Dkk\nd[rinks] = 30 Dkk\npress 'e' to exit\n")
            what = input("Enter the item you want to buy")
            if what == "w":
                orders.append("water")
                print("Water added to your tab")
                sleep(1)
                    
            elif what == "b":
                orders.append("beer")
                print("Beer added to your tab")
                sleep(1)

            elif what == "d":
                orders.append("drinks")
                print("Drink added to your tab")
                sleep(1)

            elif what == "e":
                orderList[str(orderNR)] + orders
                orderNR += 1
                order(orderNR)
                 
            else:
                print("Invalid Input")

    if addOrder == "n":
        calcStats(orderList)
    else:
        print("Invalid Input")
        sleep(1)
        order(orderNR)
    


def calcStats(orderList):
    totalPrize = 0
    totalAM = 0
    waterTAM = 0 
    beerTAM = 0
    drinksTAM = 0
    avarege = []
    count = 0
    for ordernumb,items in orderList.items():
        waterAM = 0
        beerAM = 0 
        drinksAM = 0
        count += 1
        for item in items:
            if item == "water":
                totalPrize += 10
                totalAM += 1
                waterTAM += 1
                waterAM += 1
            if item == "beer":
                totalPrize += 20
                totalAM += 1
                beerTAM += 1
                beerAM += 1
            if item == "drinks":
                totalPrize += 30
                totalAM += 1
                drinksTAM += 1
                drinksAM += 1
        totItems = waterAM + beerAM + drinksAM
        avarege.append(totItems)
        print(totalPrize)

    totalAV = 0
    for order in avarege:
        totalAV += order 


    averageAM = count / totalAV

    if waterTAM > beerTAM and waterTAM > drinksTAM:
        print("Most bought item was water with a total of: ", waterTAM, " in total")        
        sleep(1)

    if beerTAM > waterTAM and beerTAM > drinksTAM:
        print("Most bought item was beer with a total of: ", beerTAM, " in total")        
        sleep(1)

    if drinksTAM > waterTAM and drinksTAM > beerTAM:
        print("Most bought item was drinks with a total of: ", drinksTAM, " in total")        
        sleep(1)

    sleep(1)
    print("There was an average of ", totalAV, " item's pr order")
    sleep(1)
    print("Total money made today is: ", totalPrize, " Dkk")
    sleep(1)

def main():
    order(1)

main()
