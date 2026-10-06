'''
Logan Eyrich
Chapter 6
Cities
'''

# Create a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
	"Tokyo": {
		"country": "Japan",
		"population": "approximately 14 million",
		"fact": "Tokyo is home to the world's busiest pedestrian crossing.",
	},
	"Paris": {
		"country": "France",
		"population": "approximately 2 million",
		"fact": "The Eiffel Tower is in Paris.",
	},
	"Cairo": {
		"country": "Egypt",
		"population": "approximately 10 million",
		"fact": "Cairo is near the ancient pyramids of Giza.",
	},
}

# Print information about each city
for city, information in cities.items():
	print(f"\n{city}:")
	for detail, value in information.items():
		print(f"  {detail.title()}: {value}")