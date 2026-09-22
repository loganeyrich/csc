'''
Logan Eyrich
Chapter 4
Cube Numbers
'''

# Create an empty list to store the cubes
cubes = []

# Uses a for loop to calculate the cubes from 1 through 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Uses another for loop to print out the value of each cube
for cube in cubes:
    print(cube)