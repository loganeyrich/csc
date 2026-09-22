'''
Logan Eyrich
Chapter 4
Cube Comprehension
'''
# Generate a list of the first 10 cubes using a list comprehension
cubes = [number**3 for number in range(1, 11)]

# Print each value in the list
for cube in cubes:
    print(cube)