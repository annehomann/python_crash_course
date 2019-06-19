# A tuple looks just like a list except you use () instead of []
# Values cannot be changed like they can be in lists
# Simply put, a mutable object can be changed after it is created (List), and an immutable object can’t (Tuple).

# MUTABLE LIST
dimensions = [200, 50]
print(dimensions[0])
print(dimensions[1])
# value can be changed
dimensions[0] = 250
print(dimensions[0])
print(dimensions[1])

# IMMUTABLE TUPLE
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# value CANNOT be changed
# dimensions[0] = 250
# print(dimensions[0])
# print(dimensions[1])
# TypeError: 'tuple' object does not support item assignment

# For Loops can be used as normal for tuples
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)

# For Loop with tuples example
buffet = ('shrimp', 'beef', 'oysters', 'ham', 'salad')
print("\nHere's what I'm eating at the buffet: ")
for food in buffet:
    print(food)

buffet = ('shrimp', 'lamb', 'oysters', 'rice', 'salad')
print("\nHere's what I'm eating at the REVISED buffet: ")
for food in buffet:
    print(food)

