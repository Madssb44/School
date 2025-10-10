# Resturant task

# i dit program skal brugen kunne:
# Se menuen (som er gemt i en tuple)
# Lade brugeren bestille 1-flere retter.
# Se brugerens bestilling(Her skal brugen se sine retter og pris)
# Brugeren skal kunne afslutte programmet ellers skal det køre.
import time

menu = ["おにぎり", "やきにく", "すし", "おこのみやき", "踞尾の魚"]
menuPrice = [250, 150, 100, 2000, 2500]
orders = 1
done = 1
order = []
total = 0
amount = 1

while True:
    print("Welcome to 肉屋のマス")
    time.sleep(1)
    print("Here is the menu!")
    print("""                  
--------------------------------------
おにぎり 250 ¥ per piece            
やきにく 150 ¥ per piece             
すし 100 ¥ per piece
おこのみやき 2000 ¥ per meal
踞尾の魚 2500 ¥ per meal                  
--------------------------------------        

          
If you want to leave just type 'exit'          
""")

    what = input("Which item do you want to order form the menu:\n")
    if what == "exit":
        exit()
    if what in menu:
        item = menu.index(what)
        price = menuPrice[item]
        orderTemp = "1 " + what + " which costs " + str(price) + " ¥"
        order.append(orderTemp)
        total += price
        while done != 0:
            print("Can i get you anything else?")
            nextItem = input(
                "Either enter the item you want to buy or done to get your check:\n"
            )
            if nextItem in menu:
                what = nextItem
                item = menu.index(what)
                price = menuPrice[item]
                orderTemp = "1 " + what + " which costs" + str(price) + " ¥"
                order.append(orderTemp)
                total += price
            if nextItem == "done":
                print(f"You have ordered {order[0:]}")
                print(
                    f"And your total is {total} ¥ hope the food tastes good!\nAnd thanks for choosing 肉屋のマス!"
                )
                time.sleep(2)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                break
    else:
        print("Sorry i didn't quite get that could you type it again!")
        time.sleep(2)
        print("Lets start over!")
        time.sleep(2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")