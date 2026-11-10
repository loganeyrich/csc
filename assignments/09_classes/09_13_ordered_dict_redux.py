'''
Logan Eyrich
Chapter 9
Difficulty: 5/10
'''

import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

# Roll a 6-sided die 10 times
print("6-sided die:")
d6 = Die()
for i in range(10):
    d6.roll_die()

# Roll a 10-sided die 10 times
print("\n10-sided die:")
d10 = Die(10)
for i in range(10):
    d10.roll_die()

# Roll a 20-sided die 10 times
print("\n20-sided die:")
d20 = Die(20)
for i in range(10):
    d20.roll_die()