'''
Logan Eyrich
Chapter 6
People
'''
# Creates a list of dictionaries for three different people
people = [
    {
        'first_name': 'Logan',
        'last_name': 'Eyrich',
        'age': 18,
        'city': 'Philadelphia'
    },
    {
        'first_name': 'Drew',
        'last_name': 'Jones',
        'age': 22,
        'city': 'Boston'
    },
    {
        'first_name': 'John',
        'last_name': 'Garcia',
        'age': 29,
        'city': 'Chicago'
    }
]

# Prints everything known about each person
for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print() # Adds a blank line between each person's information