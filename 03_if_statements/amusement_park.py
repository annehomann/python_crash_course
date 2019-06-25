age = 12

if age < 4:
    print("Your admission price is $0.")
elif age < 18:
    print("Your admission price is $5.")
else:
    print("Your admission price is $10.")


# More concise way of writing the above code
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: # You can have as many elif statements as you'd like
    price = 10
else:
    price = 5

print("Your admission price is $" + str(price) + ".")


# You don't always have to end with an else statement
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: 
    price = 10
elif age >= 65:
    price = 5

print("Your admission price is $" + str(price) + ".")