'''
Logan Eyrich
Chapter 4 
Buffet
'''
# Store five basic foods in a tuple
buffet_foods = ("pizza", "pasta", "salad", "soup", "bread")

print("Original menu:")
for food in buffet_foods:
    print(f"- {food}")

# Try to modify one of the items (this will cause an error)
# buffet_foods[0] = "burger" (Commented out to avoid error)

# Rewrite the tuple with a new menu replacing two items (pizza and bread with tacos and burgers)
buffet_foods = ("tacos", "pasta", "salad", "soup", "burger")

print("\nRevised menu:")
for food in buffet_foods:
    print(f"- {food}")