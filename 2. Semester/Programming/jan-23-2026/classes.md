# classes in python 

## What are they 
a class is a way to define what a someting needs normally what something needs to be used in the program

## Why should we use them 
when you have a lot of things that needs to have some information assaosiated with them fx 

a character in a game 

they all need to have some information the game needs so by making a class you can then tell what a circain character has
so things like hp, mana, gold, strength, intiligence, e.t.c..

now when a new character is made it will have everything saved to their name which then can be called at any time when needed 


## How they work 
you make the class and give it some attributes which it need to forfill and then can call on later 


## Methods for working with functions 
### Making a class 
To make a class you start by defining its name and calling class fx 

class Character:

its best practice to always make classes with the first char of the name capital to diffinciate it from functions

### init
classes needs to be initilized before they work so after making it you init it like this 

class Character: (from the example before, this will be used and expanded from here when going over new things)
    def __init__(self, level, hp, mana, e.t.c..)
        self.level = level
        self.hp = hp 
        self.mana = mana 


now when defining something as Character and pass it the arguments the object will have the attributes saved to its name 

### changing things in a class
we can then define some things we can do with the class depending on how you want to use the data attributed to it fx

class Character: (from the example before, this will be used and expanded from here when going over new things)
    def __init__(self, level, hp, mana, e.t.c..)
        self.level = level
        self.hp = hp 
        self.mana = mana 

    def heal(self):
        self.hp += 10 
        print('you regained 10 hp')

    def get_hit(self, damage):
        self.hp -= damage 
        print(f"you took {damage} hp of damage")

    def show_level(self):
        print(f"you are level {self.level}")

we can now see what level we are and change and show our hp 

### using the class 
Now its time to use it all! so assuming we have imported the class we can then use it like so 

Zaarey = Character(1, 100, 15) 

Zaarey.get_hit(50)
Zaarey.show_level() 

now we have made a character and they got hit once and we have seen what level they are we can then make as many characters as we want with the Character class!
