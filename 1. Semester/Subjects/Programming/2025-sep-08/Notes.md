# How to run code
Theres 2 main ways you can run code depending on what coding language

## Compiler 
A compiler take the entire code and compiles it into a fully functional program meaning that it checks all the lines of code and if they are right it compiles them into assembly code that can be sent directly into the CPU

Compiled programs will always run faster than programs written in a Interpreter language since the translation into assembly is already done and it can execute the instructions directly 

One of the cons of working with a compiler based coding language is that its harder to test the code as you go since you will need to compile the program each time you want to run it

## Interpreter 
A interpreter reads the code its given line by line and translates it into assembly and sends it to the CPU 1 line at a time.

This makes it much easier to test code as you go since you don't have to compile an entire program just to test one part of it

But in return is also much shower than a compiled program since theres a constant back and forth with translating the code and sending the instructions to the CPU.

## What is better?
One isn't necessarily better than the other but what it comes down to is the use case of the program you are writing and how it will be used,

A Compiled program would typically be larger programs or programs that will be used form a while at a time, a example of something that wouldn't make sense to write in a compiler language would be a simple calculator that doesn't need to use a lot of processing power since it mostly deals with small and quick calculations and the time saved by writing it in a compiler language would be close to none the the code needed to write a compiled program typically is longer and harder to write.

A Interpreter program would be something that quick to run and not meant for prolonged use, something that wouldn't make any sense to write in a interpreter language would be something like a OS (Operating system) or SSH where speed and performance would be greatly it the point where it could be considered useless due to the prosing time needed for so large instructions to be translated on the fly

