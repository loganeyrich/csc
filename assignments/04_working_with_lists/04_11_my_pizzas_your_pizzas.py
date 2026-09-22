'''
Logan Eyrich
Chapter 4
My Pizzas Your Pizzas
'''
# Start with the list of pizzas
favorite = ['pepperoni', 'sausage', 'veggie']

# Make a copy of the list and call it friend, set them equal to favorite
friend = favorite[:]

# Add a new pizza to the original list
favorite.append("meat lover's")

# Add a different pizza to the friend list
friend.append('hawaiian')

# Prove that you have two separate lists by printing them
print("My favorite pizzas are:")
for pizza in favorite:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend:
    print(pizza)