'''
Logan Eyrich
Code Jam
Difficulty: 8/10
'''

import plotly.express as px
from die import Die  # Assumes the standard PCC Die class is available

# 1. Create three D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 2. Roll the dice 50,000 times and store the sum of each roll
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 3. Analyze the frequency of each possible sum (from 3 to 18)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 4. Generate the visualization
title = "Distribution of Rolling Three D6 Dice 50,000 Times"
labels = {'x': 'Total Sum of Dice', 'y': 'Frequency'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customize the x-axis to show every single integer value clearly
fig.update_layout(xaxis_dtick=1)
fig.show()