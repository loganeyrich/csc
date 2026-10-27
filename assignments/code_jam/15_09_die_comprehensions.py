'''
Logan Eyrich
Code Jam
Difficulty: 7/10
'''

import plotly.express as px
from die import Die

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# 1. Roll the dice using a list comprehension
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# 2. Analyze the frequencies using a list comprehension
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=list(poss_results), y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()