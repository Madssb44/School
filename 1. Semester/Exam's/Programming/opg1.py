name = input("Enter your name\n")
year = input("Enter your birthyear\n")

print("Name: ", name, "\n", "Born in the year: ", year)

age = 2026 - int(year)

print(f"So you must be {age} year's old!") 


if age < 25:
    print(f"What  young soul {name}")

if age <= 67 and age >= 25:
    print("Ahh still got the best years ahead of you")

if age > 67:
    print("Plenty of experiance")

