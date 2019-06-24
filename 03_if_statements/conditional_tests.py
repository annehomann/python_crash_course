car = 'suburu'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'suburu')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

fruit = 'banana'
print("\nIs fruit == 'banana'? I predict True.")
print(fruit == 'banana')

print("\nIs fruit == 'apple'? I predict False.")
print(fruit == 'apple')


soup = "pumpkin"
if soup != "tomato":
    print("I wanted tomato soup!")

flower = "tulip"
if flower != "rose" or "sunflower":
    print("Wrong flower dingus")

name = "MARCUS"
name02 = "marcus"
if name == name.upper() and name02 == name02.lower():
    print(name + " " + name02)

num1 = 15
num2 = 45
if num1 > num2:
    print("True") # This should not print anything out

if num1 < num2:
    print("True") # This should print True

if num1 >= 15:
    print("True") # This should print True

if num1 <= 25:
    print("True") # This should print True

if num1 == num2:
    print("False")

choc_bars = ['snickers', 'kitkat', 'chokito', 'mars', 'boost']

if 'snickers' in choc_bars:
    print("Yummmm")

if 'boost' in choc_bars:
    print("Gimmie :p")

if 'bounty' in choc_bars:
    print("No :(") # This won't print