# Functions
The topic for today is functions and we will be learning about what they are how to use them and why they are so useful when writing code

## What is it?
A function is some code written in a single word such as: print(), input(), etc

## Why use it?
The whole reason you would use functions in the first place is to make your code more readable and practical

The readable part comes form the function name itself, when making a function the name of it should ideally describe what the function does so that just by reading the function name you can ascertain what the result of using it will be, but while that isn't always something that you can do since some functions can get more complicated its a good base rule to try and name functions in such a way!

The practical reason for using functions is that any line of code that you are gonna use more than once can be called with a function instead of having to write the it over and over again, this could be used if a calculation would be done from different places in the code depending on where in the program the user is, if you don't use functions you would have to write the entire code of the function in each part of the code that would need it while if you were to use functions it would just be the function definition you made that would need to be called, this also makes it easier to expand the program it the function ever needs to be used in a newer part of the program it could just be called with the function instead of having to write the code for the new part again

## How to make one!
When making a function theres a few rules to follow depending on the language you are writing a function for, since the school focuses on python thats what ill describe.

When starting a function you need to define it give it a name and end it with a colon
- def \<name\>():

def stands for define meaning that you are defining the thing that comes after <br>
The name should describe what the function does, this is the name you need to call when you wanna use the function <br>
() indicates that its a function and is where you would add the arguments if needed <br>
: is used to show that the following part is called when the function is used

So how to put it all together

```
def adding():   
        num1 = 1
        num2 = 1
        total = num1 + num2
        print(total)

adding()

```

This is a simple function that adds 1 and 1 together and prints the result when called! so following the guidelines set earlier, suing def to indicate we are defining something, 'adding' being the name of the function since its adding something together, () to show its a function and : to indicate that when called its the following code thats being called into use.

## Parameters
Functions can have parameters which are information needed to execute the code, the parameters will be indicated in the definition you make for the function, using the same example as before:

```
def adding(number1, number2):   
        total = number1 + number2
        print(total)

adding(2,3)

```
The arguments number1 & number2 now indicates that it needs a 2 numbers to work and when called with 2 & 3 as shown above would then add number1 (2) and number2 (3) and then print total (5) allowing you to now insert any 2 numbers you want added together!

Parameters much like the function itself should also be named to indicate what kind of information its expecting as well as having some best practices to even further indicate the datatype using the example above and adding best practices to it would look like this: 


```
def adding(number1: int, number2: int) -> None:   
        total = number1 + number2
        print(total)

adding(2,3)

```

While changing nothing about how the actual code works it now shows that number1 & number2 are expecting a int and the -> shows that the return from the function is None

Here you can of course use all the different types of data like: int, str, bool, float, e.t.c.. <br>
To indicate the expected datatype and the -> can also be set depending on what the function returns like -> Ture: -> str: -> int: -> float: e.t.c.. 

## Return
A return is something thats coming out of a function or what its returning after use.

A return can be any datatype and as shown above should be indicated for ease of use / readability and is used when a function needs to process something and give back the result of set processed information

This can be everything form complex calculations to simple adding a number in the middle of something and returning it or sending some data and seeing if it fits the parameters the function is checking for and returning True or False

The reason to indicate what datatype the return gives is so that when a program grows too large to remember everything about every function you have created you still have a easy way to know how to use the function without having to go back and reading it to find out what it returns

so a example of how a return could made using the example from earlier would be:

```
def adding(number1: int, number2: int) -> str:   
        total = number1 + number2
        return str(total)

print(adding(2,3))
```

Now instead of printing the total from the function it how returns a the str that the print then prints outside of the function, you can also define a new variable as the return by doing: 'VARIABLE = adding(2,3)' now the return from adding is stored in VARIABLE and can be use for the print or what the next process its needed for.

## Local Vs Global
variables are used all over code but when working with functions theres a few things you need to keep in mind!


### Local Variables
When you make a variable within a function its whats know as a local variable, meaning that its only know withing the function and can't be accessed outside the function itself, this has a few positives and negatives

The Positive is that the same named variable can be used over and over again by different functions without having to worry about it already having information stored in them eliminating the need to always find more and more names for variables the larger the program become

The negative is that whenever theres something you need to get out form the come it needs to be returned from the function and sent as a argument to the next function that needs the data

### Global Variables
The one way you can circumvent this is by making it a global variable meaning that the variable is now known globally throughout the entire program, just like local variables this also has some positives and negatives.

The positive of making a variable global is that you don't need to have it as a argument in every function that needs it to work allowing you to process it no matter where in your code you are and how much its been changed

The negative is that the name you gave it now is taken and can't be used anywhere else in the code and the data stored in tha variable now can change without you knowing what datatype it is making it more risky to work with if it can be different datatype's depending on how its been processed from the previous function thats used it

## main()
When writing a program its normal to do almost every process through functions and then running the entire program from a main function or main()

This is done to have a readable overview of how a program runs from just by reading the main function and then being able to go out and reading the separate functions if needed, Its also commonly the main function what will run the main loop of the program to ensure that it always runs or keeps running after a function is done, of course depending on the type of program thats being used, and if a main function includes a loop its of course a must to have a function or way to exit the program as to not lock user into it