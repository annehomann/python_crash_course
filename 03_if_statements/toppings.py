available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives', 'tomato']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'anchovies']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


# If the list is empty. Python returns True if the list contains at least one item
# An empty list evaluates to False
# Because of the empty list, the conditional test fails so it skips the for loop
requested_cars = []

if requested_cars:
    for requested_car in requested_cars:
        print("Adding " + requested_car + "to your garage.")
    print("\nFinsihed adding cars to garage")
else:
    print("\nAre you sure you don't want a car?")

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping) # Displays true items in list
    else:
        print("We do not have " + requested_topping + " available") # Picks up the false item in list
    
print("\nFinished making your pizza!")