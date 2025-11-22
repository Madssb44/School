# Resturant task

# i dit program skal brugen kunne:
# Se menuen (som er gemt i en tuple)
# Lade brugeren bestille 1-flere retter.
# Se brugerens bestilling(Her skal brugen se sine retter og pris)
# Brugeren skal kunne afslutte programmet ellers skal det køre.
import time

menu = [("おにぎり", 250),("やきにく", 150),("すし", 100),("おこのみやき", 2000),("踞尾の魚", 2500)]

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
--------------------------------------""")
    for item_name, item_price in menu:
        print(f"{item_name} {item_price} ¥ per piece/meal")
    print("""--------------------------------------        

          
If you want to leave just type 'exit'          
""")

    what = input("Which item do you want to order form the menu:\n")
    if what == "exit":
        exit()
    
    # Find the item in the menu
    found_item = None
    for item_name, item_price in menu:
        if item_name == what:
            found_item = (item_name, item_price)
            break
    
    if found_item:
        item_name, price = found_item
        orderTemp = "1 " + item_name + " which costs " + str(price) + " ¥"
        order.append(orderTemp)
        total += price
        
        while done != 0:
            print("Can i get you anything else?")
            nextItem = input(
                "Either enter the item you want to buy or done to get your check:\n"
            )
            
            # Check if nextItem is in the menu
            found_next = None
            for item_name, item_price in menu:
                if item_name == nextItem:
                    found_next = (item_name, item_price)
                    break
            
            if found_next:
                item_name, price = found_next
                orderTemp = "1 " + item_name + " which costs " + str(price) + " ¥"
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
