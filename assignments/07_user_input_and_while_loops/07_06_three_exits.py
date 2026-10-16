'''
Logan Eyrich
Chapter 7
Three Exits
'''

# This program demonstrates the use of a while loop with three exit conditions.
# Initialize the variable with an empty string so the loop starts
topping = ""
print("Enter 'quit' when you are finished.")
while topping != 'quit':
    topping = input("What topping would you like on your pizza? ")
    if topping != 'quit':
        print(f"  Adding {topping} to your pizza!")