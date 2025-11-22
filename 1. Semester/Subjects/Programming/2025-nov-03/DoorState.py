
# Start with short description
#
# Locked state
# Testing stage with 2 returns depending on password 
# Unlocked stage that can lock it again
from time import sleep
import hashlib

def makingAFunnyPassword():
    global superDuperHiddenPassword
    toEncrypt = "admin"
    superDuperHiddenPassword = hashlib.sha256(hashlib.sha256(toEncrypt.encode()).hexdigest().encode()).hexdigest()

def greeting():
    print("Hello World!")
    sleep(1)

def locked(state):
    global attempts
    print("The current stage is Locked to gain access follow the instructions")
    attempts = 3
    while attempts > 0:
        sleep (1)
        state = input("Enter a valid password to progress to unlocked: ")
        return checking(state)
        
        
def checking(state):
    global attempts
    print("Checking password")
    sleep (1)
    if state == superDuperHiddenPassword:
        state = "unlocked"
        return unlocked(state)
    elif state != superDuperHiddenPassword:
        print("\nWRONG\n")
        sleep(1)
        attempts -= 1
        state = "locked"
        return locked(state)
    
    
def unlocked(state):
    print("Great job guessing my password!")
    sleep(2)
    print("\nSystem now unlocked!")
    sleep(2)
    while True:
        funny = input("Well theres nothing here to do other than typing random stuff or locking the system again so have fun!\n\n")
        sleep(2)
        if funny == "lock":
            state = "locked"
            return locked(state)
        else:
            print("\nSee ins't this fun!")
            sleep(3)
            print("\nNow back to the other message for a even more wonderful time typing stuff in!")
            sleep(3)
            print("\nOh and if you want to lock the system again just type 'lock'")
            sleep(0.5)
            print("\n" * 100000000)


def main():
    global attempts
    makingAFunnyPassword()
    state = "locked"
    stage = locked
    attempts = 3
    greeting()
    while True:
        stage = stage(state)
while True:
    main()

























































































































# for when you are done guessing >:D 998ed4d621742d0c2d85ed84173db569afa194d4597686cae947324aa58ab4bb
