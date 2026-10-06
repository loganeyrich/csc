'''
Logan Eyrich
Chapter 6
Favorite Places
'''

# Create a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person as a list. Loop through the dictionary, and print each person's name and their favorite places.
favorite_places = {
	"Evan": ["Japan", "Paris", "Italy"],
	"Drew": ["Yosemite", "Florida", "Germany"],
	"Stanley": ["New York City", "The Mountains", "The Beach"],
}

for person, places in favorite_places.items():
	print(f"\n{person}'s favorite places are:")
	for place in places:
		print(f"{place}")