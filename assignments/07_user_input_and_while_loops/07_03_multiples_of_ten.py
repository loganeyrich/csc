'''
Logan Eyrich
Chapter 7 
Multiples of Ten
'''

# This program prints the multiples of ten from 10 to 100.
# Asks the user for a number
number = input("Please enter a number: ")

# Converts the input string into an integer
number = int(number)

# Checks if the number is a multiple of 10
if number % 10 == 0:
    print(f"Yes, {number} is a multiple of 10.")
else:
    print(f"No, {number} is not a multiple of 10.")