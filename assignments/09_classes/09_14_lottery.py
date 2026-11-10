'''
Logan Eyrich
Chapter 9
Difficulty: 6/10
'''

from random import choice

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_ticket = []
while len(winning_ticket) < 4:
    selected_item = choice(lottery_pool)
    if selected_item not in winning_ticket:
        winning_ticket.append(selected_item)
print("Any ticket matching these 4 numbers or letters wins a prize:")
print(winning_ticket)