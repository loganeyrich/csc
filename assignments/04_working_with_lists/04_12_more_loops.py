'''
Logan Eyrich 
Chapter 4
More Loops
'''

# Start with the list of pizzas from Exercise 4-11
favorite = ['pepperoni', 'sausage', 'veggie']

# Make a copy of the list and call it friend
friend = favorite[:]

# Add a new pizza to the original list
favorite.append("meat lover's")

# Add a different pizza to the friend list
friend.append('hawaiian')

# Prove that you have two separate lists by printing each list with a for loop
print("My favorite pizzas are:")
for pizza in favorite:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend:
    print(pizza)