# making a function that will take a random number between 1-100 
# the user needs to guess the number and the program will tell if its higher or lower
# when the user guesses right the program will tell how many guesses it takes
import random
from time import sleep

def guess_a_number(goal,guesses):
            while goal:
                sleep(0.5)
                guess = int(input("Enter your guess: "))
                if guess == goal:
                    guesses += 1
                    print(f"\nCongrats you guessed it right!\nYou used {guesses} guesses")
                    sleep(2)
                    print("\n"*10)
                    goal = False
                elif guess < goal:
                    print("\nYour guess was too low!\n")
                    sleep(1)
                    guesses += 1
                    guess_a_number(goal,guesses)
                elif guess > goal:
                    print("\nYour guess was too heigh\n")
                    sleep(1)
                    guesses += 1
                    guess_a_number(goal,guesses)
            print("welcome to the guessing game!\nI have chosen a number between 1 and 100\n\nHave fun guessing it!")
            goal = random.randrange(1,100)
            guesses = 0
            sleep(1)
            guess_a_number(goal,guesses)        
        
            
    
guess_a_number(False,0)