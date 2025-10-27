# known recipe for 4 people
flourFor4 = 250
milkFor4 = 4
eggsFor4 = 3 

# Make a function to get the value for the ammount of people the user wantes
# Then calculates how much they need and print it in a readable format
# if either 4 or 1 is the ammount it will take the already known values and print with instead to not need to do a extre calcualtion
def pancakesForX(people):
    if people != 4 or 1:   
        flour = flourFor4 / 4 * people
        milk = milkFor4 / 4 * people
        eggs = eggsFor4 / 4 * people
        
        print(f"""
    To make pancakes for {people} people you need: 

    {flour} grams of flour
    {milk} dl of milk
    {eggs} eggs""")
    elif people == 4:
        print(f"""
To make pancakes for {people} people you need: 

{flourFor4} grams of flour
{milkFor4} dl of milk
{eggsFor4} eggs""")


# main loop to keep the code running
def main():
    while True:
        print("\n"*5)
        people = int(input("Enter the ammount of people you want to make pancakes for: "))
        pancakesForX(people)
        
        
main()