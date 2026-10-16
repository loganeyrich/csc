'''
Logan Eyrich
Chapter 7
Movie Tickets
'''

# Creates a while loop that asks users their age and tells them the price of their movie ticket based on their age. The loop continues until the user types 'quit'.
active = True
while active:
    age = input("What is your age? (Enter 'quit' to exit) ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
