'''
Logan Eyrich
Chapter 7
Deli
'''

# Create a list called sandwich_orders and fill it with the names of various sandwiches. Then create an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
# List of sandwich orders
sandwich_orders = ["tuna", "roast beef", "turkey", "grilled cheese", "veggie"]

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the orders, make each sandwich, and move it to finished_sandwiches
while sandwich_orders:
  current_sandwich = sandwich_orders.pop(0)  # or .pop() for last-in, first-out
  print(f"I made your {current_sandwich} sandwich.")
  finished_sandwiches.append(current_sandwich)

print("\nAll of these sandwiches have been made:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich} sandwich")