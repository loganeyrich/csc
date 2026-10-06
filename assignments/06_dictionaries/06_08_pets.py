'''
Logan Eyrich
Chapter 6
Pets
'''

pets = [
	{'kind': 'dog', 'owner': 'Logan'},
	{'kind': 'cat', 'owner': 'Drew'},
	{'kind': 'bunny', 'owner': 'Alex'},
]

for pet in pets:
	print(f"\nAnimal: {pet['kind'].title()}")
	print(f"Owner's name: {pet['owner'].title()}")

