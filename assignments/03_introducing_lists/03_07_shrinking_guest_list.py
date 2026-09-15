'''
Logan Eyrich
Chapter 3
Shrinking Guest List
'''

# Creates a list of guests and prints a message for each guest in the list
guests = ['Robert Patterson', 'Kanye West', 'Lebron James']
message1 = guests[0] + ', you are invited to dinner at my house.'
message2 = guests[1] + ', you are invited to dinner at my house.' 
message3 = guests[2] + ', you are invited to dinner at my house.'
print(message1)
print(message2)
print(message3)

#  Inserts 3 guests to the list of guests and appends one guest to the end of the list, then prints a message for each guest in the updated list
guests.insert(0, 'Tom Brady')
guests.insert(2, 'Dwayne Johnson')
guests.append('Drake')

# Creates a new list of guests and prints a message for each guest in the new list
message1 = guests[0] + ', you are invited to dinner at my house.'
message2 = guests[1] + ', you are invited to dinner at my house.'
message3 = guests[2] + ', you are invited to dinner at my house.'
message4 = guests[3] + ', you are invited to dinner at my house.'
print(message1)
print(message2)
print(message3)
print(message4)

# List can only contain two guests, so a message is printed to indicate that the guest list must be shrunk
print('\n' + 'I can only invite two guests to dinner.' + '\n')
removed_guests = guests.pop(0)
print('I am sorry, ' + removed_guests + ', but I cannot invite you to dinner.')
removed_guests2 = guests.pop(1)
print('I am sorry, ' + removed_guests2 + ', but I cannot invite you to dinner.')
removed_guests3 = guests.pop(1)
print('I am sorry, ' + removed_guests3 + ', but I cannot invite you to dinner.')
removed_guests4 = guests.pop(1)
print('I am sorry, ' + removed_guests4 + ', but I cannot invite you to dinner.')

# Prints a message to the two guests still on the list
print(guests[0] + ', you are still invited to dinner.')
print(guests[1] + ', you are still invited to dinner.')

# Deletes the two guests still on the list and prints the empty list
del guests[0]
del guests[0]

# Prints the empty list
print(guests)