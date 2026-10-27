'''
Logan Eyrich
Code Jam
Difficulty: 8/10
'''

import plotly.express as px
from random import randint

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and num_sides."""
        return randint(1, self.num_sides)

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Make 50,000 rolls and store the products in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the frequencies of each possible outcome
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = list(range(1, max_result + 1))

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Customize and render the visualization
title = "Results of Multiplying Two D6 Dice Rolls (50,000 Rolls)"
labels = {'x': 'Product of Two Dice', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Force the X-axis to display every single number integer step
fig.update_layout(xaxis_dtick=1)
fig.show()