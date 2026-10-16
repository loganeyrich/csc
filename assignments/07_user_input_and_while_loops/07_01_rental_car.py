'''
Logan Eyrich
Chapter 8
Rental Car
'''

# Prompt the user for a rental car and print a message about it. If the user doesn't enter a valid car type, prompt them again until they do.
while True: 
    rental_car = input("What kind of rental car would you like? ")
    if rental_car:
        print(f"Let me see if I can find you a {rental_car}.")
        break
    else:
        print("Please enter a valid car type.")