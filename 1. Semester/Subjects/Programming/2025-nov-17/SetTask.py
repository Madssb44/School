# see who showed ip
# who didn't show up
# of the people who showed up, was on the atteners list


attenders = {"Anna","Mads","Sara"}
showedUp = {"Sara","Anna","Leif","kaj"}

# listing who was supposed to attend
print("Who was supposed to show up: ")
for person in attenders:
    print(person)


# listing who showed up
print("\nPeople who showed up: ")
for person in showedUp:
    print(person)
    
print("\nDid everyone who was supposed to show up attend?")
if not showedUp.issubset(attenders):
    if attenders != showedUp:
        print("No not everyone showed up...")
        for name in attenders:
            if name not in showedUp:
                print(f"{name} is missing")
        
if not attenders.issubset(showedUp):
    print("\nSome people weren't supposed to be here their names are: ")
    for name in showedUp:
        if name not in attenders:
            print(f"{name} ins't supposed to be here")
