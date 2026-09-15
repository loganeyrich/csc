'''
Logan Eyrich
Chapter 3
Seeing the World
'''

# Creates a list of locations and prints the list
locations = ['Japan', 'Germany', 'Switzerland', 'Peru', 'France']
print(locations)

# Prints the list in alphabetical order without changing the original list
print(sorted(locations))
print(locations)

# Prints the list in reverse alphabetical order without changing the original list
locations.sort(reverse=True)
print(locations)

# Reverses the order of the list
locations.reverse()
print(locations)

# Reverses the order of the list again to return it to its original order
locations.reverse()
print(locations)

# Changes the list so it is stored in alphabetical order
locations.sort()
print(locations)

# Changes the list so it is stored in reverse alphabetical order
locations.sort(reverse=True)
print(locations)