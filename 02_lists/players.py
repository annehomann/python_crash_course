# Slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:6])

# Without the first index, :n will give you the first entries of the list 
# until you specify a stopping point
print(players[:3])
# E.g. From the start of the list until index[2]
# ['charles', 'martina', 'michael']

# Without the last index, :n will give you the entries starting from the specified 
# index until the end of the list
print(players[2:])
# E.g. From index[2] until the end of the list
# [michael', 'florence', 'eli']

print(players[-3:])
# Using negatives means accessing the end of the list first and going backwards
# E.g. Working backwards from the end of the list
# [michael', 'florence', 'eli']

print("Here are my first three players: ")
for player in players[:3]:
    print(player.title())