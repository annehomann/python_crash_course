cars = ['bmw', 'audi', 'toyota', 'subaru']
""" # Sorts list alphabetically
cars.sort() 
print(cars)
# Reverses list alphabetically
cars.sort(reverse=True) 
print(cars) """

# sorted() function for temporary alphabetical sorting
""" print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ") 
print(cars) """

# Printing a list in Reverse Order (as set out in list)
# Changes the order of a list permanently, but you can revert to the original 
# order anytime by applying reverse() to the same list a second time
print(cars)
cars.reverse()
print(cars)
cars.reverse() # reverts the list back to it's original setting
print(cars)

# Finding the length of a list 
print(len(cars))
# 4