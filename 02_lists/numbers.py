""" for value in range (1,11):
    print (value) """

# Takes numbers 1-10 and inputs them into a list
numbers = list(range(1,11))
print(numbers)

# Skipping numbers in a range
# Starts with the value 2, adds 2 to the value until it reaches the final value of 11
even_numbers = list(range(2,11,2))
print(even_numbers)
# # Starts with the value 1, adds 2 to the value until it reaches the final value of 11
# In both examples, the last value of 2 in the range is what increases each by 2
odd_numbers = list(range(1,11,2))
print(odd_numbers)

test_numbers = list(range(0,101,10))
print(test_numbers)