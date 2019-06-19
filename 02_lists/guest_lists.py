dead_guests = ["charles manson", "princess diana", "steve jobs"]
print(dead_guests)

print("\nI would find " + dead_guests[0].title() + " interesting because of his thoughts.")
print("I would ask " + dead_guests[1].title() + " what she was thinking marrying Prince Charles.")
print("I would pick " + dead_guests[2].title() + "' brain and overload him with questions.")


print("\nOf course " + dead_guests[0].title() + " can't make it to dinner....ughh")

del dead_guests[0]
dead_guests.insert(0, "chester bennington")

print("\nI would pick " + dead_guests[0].title() + " so we can talk about similar situations then give him a hug.\n")
print(dead_guests)

print("\nOoooo I found a bigger table! I'll invite others!\n")

dead_guests.insert(1, "chris cornell")
dead_guests.append("edith windsor")
print(dead_guests)

print("\nFFS the table won't arrive in time. Soz guys, only two of you can come....")
popped_guest = dead_guests.pop(1)
print("\nSorry " + popped_guest.title() + " but there's no room for you at dinner.")
popped_guest = dead_guests.pop(1)
print("\nSorry " + popped_guest.title() + " but there's no room for you at dinner.")
popped_guest = dead_guests.pop(1)
print("\nSorry " + popped_guest.title() + " but there's no room for you at dinner.")
print(dead_guests)
print(len(dead_guests))

## NOTES ##
# Only one varibale needed for the 'popping' rather than 3 separate varibales
# The varibale "popped_guest" can be reused as each value that is popped is no longer needed 
# So the next popped value writes over the previous one (like a loop)