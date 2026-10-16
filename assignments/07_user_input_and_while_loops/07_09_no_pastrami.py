'''
Logan Eyrich 
Chapter 7
No Pastrami
'''

# This program demonstrates the use of while loops and user input to manage a list of sandwich orders, specifically handling the case where pastrami is no longer available.
sandwich_orders = [
    'pastrami',
    'tuna',
    'pastrami',
    'turkey',
    'roast beef',
    'pastrami',
    'grilled cheese',
]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami today.\n")

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

while sandwich_orders:
  current_sandwich = sandwich_orders.pop(0)
  print(f"I'm working on your {current_sandwich} sandwich.")
  finished_sandwiches.append(current_sandwich)

print("\nAll of these sandwiches have been made:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")