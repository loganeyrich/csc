'''
Logan Eyrich
Chapter 7
Pizza Toppings
'''

# Creates a while loop that asks users for pizza toppings and adds them to a list. The loop continues until the user types 'quit'.
pizzas = True
while pizzas:
    topping = input("What topping would you like on your pizza?")
    if topping == 'quit':
        pizzas = False
    else:
        print(f"Adding {topping} to your pizza.")