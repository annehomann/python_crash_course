# My empty list called 'squares'...
squares = []
# For each value in my range of 1-10...
for value in range(1,11):
    # square each value and add each answer in the varibale of 'square'
    square = value**2
    # at the end of each for loop, append my answer to my 'squares' list
    squares.append(square)

# Print my full list of answers
print(squares)


# MORE CONCISE WAY OF WRITING THE CODE ABOVE
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)


# USING LIST COMPREHENSION
squares = [value**2 for value in range(1,11)]
print(squares)




digits = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(min(digits))
print(max(digits))
print(sum(digits))