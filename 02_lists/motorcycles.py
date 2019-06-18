""" motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) """

""" motorcycles[0] = 'ducati' #replaces index 0 value (from honda to ducati)
print(motorcycles) """

""" motorcycles.append('ducati') # An 'append statement'
print(motorcycles)
print(motorcycles.append('triumph')) # Why doesn't this work?! Because it needs to be an 'append statement'


nba_teams = []
nba_teams.append('new york knicks')
nba_teams.append('phoenix suns')
nba_teams.append('toronto raptors')
nba_teams.append('boston celtics')

print(nba_teams) """

""" shoes = ['nike', 'puma', 'adidas']
print(shoes)

shoes.insert(0, 'new balance')
print(shoes)

del shoes[3] # deletes an item from list
print(shoes) """

""" cars = ['audi', 'bmw', 'jeep', 'toyota', 'mazda','hyundai', 'nissan', 'suzuki', 'ford', 'holden', 'mercedes']
popped_cars = cars.pop()
print(cars)
print(popped_cars)

first_car = cars.pop(6)
message = "The first car I owned was a " + first_car.upper() + "."
print(message)
print(cars) """

ice_cream = ['chocolate', 'vanilla', 'banana', 'strawberry', 'coconut']
ice_cream.remove('banana') # Removing by value rather than by index
print(ice_cream)

yuck = 'coconut'
ice_cream.remove(yuck)
print(ice_cream)
print("Nobody likes " + yuck + " so I removed it.")