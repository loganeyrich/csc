'''
Logan Eyrich
Chapter 3
More Guests
'''

# Creates a list of guests and prints a message for each guest in the list
guests = ['Jalen Hurts', 'Kanye West', 'Lebron James']
message1 = guests[0] + ', you are invited to dinner at my house.'
message2 = guests[1] + ', you are invited to dinner at my house.' 
message3 = guests[2] + ', you are invited to dinner at my house.'
print(message1)
print(message2)
print(message3)
# Prints a message that one of the guests cannot make it to dinner
print('Unfortunately, Jalen Hurts cannot make it to dinner.' + '\n')

# Creates a new list of guests and prints a message for each guest in the new list
guests2 = ['Robert Patterson', 'Kanye West', 'Lebron James']
message1 = guests2[0] + ', you are invited to dinner at my house.'
message2 = guests2[1] + ', you are invited to dinner at my house.' 
message3 = guests2[2] + ', you are invited to dinner at my house.'
print(message1)
print(message2)
print(message3)

# The first section of the program has ended, and a message is printed to indicate that more guests will be invited to dinner
print('This program has ended.')
print('I found a bigger dinner table, so I am inviting more guests to dinner.' + '\n')
# Inserts two new guests into the list of guests and appends one new guest to the end of the list, then prints a message for each guest in the updated list
guests2.insert(0, 'Tom Brady')
guests2.insert(2, 'Dwayne Johnson')
guests.append('Drake')
# Creates a new list of guests and prints a message for each guest in the new list
message1 = guests2[0] + ', you are invited to dinner at my house.'
message2 = guests2[1] + ', you are invited to dinner at my house.'
message3 = guests2[2] + ', you are invited to dinner at my house.'
message4 = guests2[3] + ', you are invited to dinner at my house.'
message5 = guests2[4] + ', you are invited to dinner at my house.'
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)