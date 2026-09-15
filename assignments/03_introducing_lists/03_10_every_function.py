'''
Logan Eyrich
Chapter 3
Every Function
'''

# Creating a list of comic book characters
# Uses every function to manipulate the list and print the results for lists
characters = ['Spider-man', 'Batman', 'Superman', 'Nova', 'Radiant Black', 'Iron Man']
print(characters)
print(sorted(characters))
print(sorted(characters, reverse=True))
characters.reverse()
print(characters)
print('There are ' + str(len(characters)) + ' characters in the list.')