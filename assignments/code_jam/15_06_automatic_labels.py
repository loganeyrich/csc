'''
Logan Eyrich
Code Jam
Difficulty:
'''

from die import Die
import plotly.express as px

# Create two D8 dice
die_1 = Die(8)
die_2 = Die(8)

# Store results for 1,000 rolls
results = []
for roll_num in range(1000):
  result = die_1.roll() + die_2.roll()
  results.append(result)