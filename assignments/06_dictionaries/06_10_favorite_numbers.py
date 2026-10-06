'''
Logan Eyrich
Chapter 6
Favorite Numbers
'''

'''
Logan Eyrich
Chapter 6
Favorite Numbers
'''

# Creates a dictionary with names as keys and lists of favorite numbers as values
numbers = {
	'Logan': [48, 16],
	'Drew': [8, 23],
	'Alex': [28, 4],
	'Evan': [2, 14],
	'Zach': [12, 31],
}
# Creates a for loop that iterates through the dictionary and prints each person's name and their favorite numbers
for name, favorite_numbers in numbers.items():
	print(name + "'s favorite numbers are " + ", ".join(map(str, favorite_numbers)) + ".")