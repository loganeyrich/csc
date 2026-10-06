'''
Logan Eyrich
Chapter 6
Rivers
'''

# Creates a dictionary of rivers and the countries they run through
rivers = {'Nile': 'Egypt', 'Amazon': 'Brazil', 'Mississipi': 'United States'}
# Creates for loops for each of the sections, giving a message for the river runs through the country, printing the river names, and printing the country names
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
