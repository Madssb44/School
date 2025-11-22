# Print tal fra 1 til 100. Hvis et tal er deleligt med 3, print "Fizz".
# Hvis deleligt med 5, print "Buzz". Hvis begge, print "FizzBuzz"

# for loop og modus % er gode at bruge i den her.

for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0 :
        print(f"{i} FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} Fizz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
    else:
        print(i)
