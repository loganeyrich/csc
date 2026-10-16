'''
Logan Eyrich
Chapter 7
Dream Vacation
'''

# This program asks the user for their dream vacation destination and then prints a message about it.
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Store each person's dream vacation destination.
destinations = []

repeat = "yes"
while repeat.lower() == "yes":
    # Ask the user where they'd like to go.
    place = input(place_prompt)

    # Store the destination.
    destinations.append(place)

    # Ask if someone else wants to respond.
    repeat = input(continue_prompt)

# Show results of the survey.
print("\n--- Results ---")
for place in destinations:
    print(f"Someone would like to visit {place.title()}.")
    