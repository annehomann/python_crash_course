my_foods = ['pizza', 'falafel', 'carrot cake', 'fairy bread']
friend_foods = my_foods[:]
# The [:] copies thelist to a new variable

my_foods.append('ice cream')
friend_foods.append('cannoli')

print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are: ")
print(friend_foods)
# Output will append each separately to its respective list
# My favourite foods are:
# ['pizza', 'falafel', 'carrot cake', 'fairy bread', 'ice cream']

# My friend's favourite foods are: 
# ['pizza', 'falafel', 'carrot cake', 'fairy bread', 'cannoli']

for i in my_foods:
    print("I love " + i)

for i in friend_foods:
    print("\nMy mate loves " + i)

""" # Trying to copy a list with the [:] doesn't work
my_foods = ['pizza', 'falafel', 'carrot cake', 'fairy bread']
friend_foods = my_foods
# When you try to append different values to each, it won't work
my_foods.append('ice cream')
friend_foods.append('cannoli')

print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are: ")
print(friend_foods)
# Output will attached both to each
# My favourite foods are:
# ['pizza', 'falafel', 'carrot cake', 'fairy bread', 'ice cream', 'cannoli']

# My friend's favourite foods are: 
# ['pizza', 'falafel', 'carrot cake', 'fairy bread', 'ice cream', 'cannoli'] """