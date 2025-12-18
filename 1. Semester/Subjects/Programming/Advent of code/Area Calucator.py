from math import pi


def areaMenu(totalArea: int) -> int:
    while True:
        try:
            if totalArea < 0:
                print(f"Current registered m² is {totalArea}\n\n")
        except NameError:
            pass
        print(
            "Pick from the following options\n1 = Square\n2 = Circle\n3 = Continue to material choice\n "
        )
        match input():
            case "1":
                totalArea += fourSidedAreaCalc()
            case "2":
                totalArea += circleCalc()
            case "3":
                materialChoice(totalArea)
            case _:
                print("Invalid input")


def fourSidedAreaCalc() -> float:
    """
    Calculates the m² of a 4 sided room/area

    can calculate for different shapes of a 4 sided area

    returns m² as a float"""

    match input(
        "Pick which option fits the room you are calculating for\n1 = Square\n2 = Rectangle\n"
    ):
        case "1":
            totalArea = squareCalc()
            return totalArea
        case "2":
            totalArea = rectangleCalc()
            return totalArea


def squareCalc() -> float:
    """Calculates the m² of a square"""
    try:
        length = float(input("Enter the length measurement in meters: "))
    except ValueError:
        print("Invalid input")
        return
    area = length * length
    return area


def rectangleCalc() -> float:
    """Calculates the m² of a square"""
    try:
        length = float(input("Enter the length measurement in meters: "))
        width = float(input("Enter the width measurement in meters: "))
    except ValueError:
        print("Invalid input")
        return
    area = length * width
    return area


def circleCalc() -> int:
    """Takes the radius of a circle and returns the m²"""
    try:
        radius = float(input("Enter the radius of the circle in meters: "))
    except ValueError:
        print("Invalid input")
        return

    area = pi * radius**2
    return area


def materialChoice(totalArea: float) -> int | dict | dict:
    Area = totalArea
    totalStone = {"Price": 0, "Amount": 0, "Area": 0}
    totalWood = {"Price": 0, "Amount": 0, "Area": 0}

    while totalArea > 0:
        print(f"""
Select a material, you will then be asked the amount you want to buy in  m².
            
Materials available currently are:
            
1 = Wood 
2 = Stone
Material needed for {totalArea} m² remaining

""")
        match input():
            case "1":
                totalArea = buyWood(totalArea, totalWood)
            case "2":
                totalArea = buyStone(totalArea, totalStone)
    doneMenu(Area, totalWood, totalStone)


def buyWood(totalArea: int, totalWood: dict) -> int | dict:
    """Calculates price/amount of planks to buy
    returns totalArea, WoodPrice, plankAmount"""

    print(f"Remaining materials needed {totalArea}\n")
    try:
        amount = float(input("Enter the area in m²: "))
    except ValueError:
        print("Invalid input")
        return
    totalArea -= amount
    totalWood["Price"] += 8 * 7 * amount
    totalWood["Amount"] += 8 * amount
    totalWood["Area"] += amount
    return totalArea


def buyStone(totalArea: int, totalStone: dict) -> int | dict:
    """Calculates price/amount of Stone to buy
    returns totalArea, stonePrice, stoneAmount"""

    print(f"Remaining materials needed {totalArea}\n")
    try:
        amount = float(input("Enter the area in m²: "))
    except ValueError:
        print("Invalid input")
        return
    totalArea -= amount
    totalStone["Price"] += 5 * 1 * amount
    totalStone["Amount"] += 5 * amount
    totalStone["Area"] += amount
    return totalArea


def doneMenu(Area: int, totalWood: dict, totalStone: dict) -> None:
    """Calculates the total price and prints information of the results"""

    total = totalWood["Price"] + totalStone["Price"]
    print(f"""
Total Area in m² = {Area}


Total price for wood bought = {totalWood["Price"]}$
Area in m² worth of wood bought = {totalWood["Area"]} m²
Total amount of planks bought = {totalWood["Amount"]}


Total price for stone bought = {totalStone["Price"]}$
Area in m² worth of stone bought = {totalStone["Area"]} m²
Total amount of stone tiles bought = {totalStone["Amount"]}


Total price for all materials bought = {total}$

""")
    match input(
        "To run the program again press '1'\nTo exit the program press anything else"
    ):
        case "1":
            areaMenu(0)
        case _:
            exit()


def main():
    while True:
        areaMenu(0)


main()


