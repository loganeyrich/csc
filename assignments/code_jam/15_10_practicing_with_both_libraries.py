'''
Logan Eyrich
Code Jam
Difficulty: 10/10
'''

import random
import matplotlib.pyplot as plt

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return random.randint(1, self.num_sides)

# 1. Create a 6-sided die
die = Die()

# 2. Roll the die 1,000 times and store results
results = [die.roll() for _ in range(1000)]

# 3. Analyze the results (count frequencies)
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]
poss_results = list(range(1, die.num_sides + 1))

# 4. Visualize the frequencies with Matplotlib
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 5))

# Create a bar chart
bars = ax.bar(poss_results, frequencies, color='skyblue', edgecolor='black', alpha=0.8)

# Customize chart text and labels
ax.set_title("Results of Rolling One D6 1,000 Times", fontsize=16, fontweight='bold')
ax.set_xlabel("Result", fontsize=12)
ax.set_ylabel("Frequency of Result", fontsize=12)
ax.set_xticks(poss_results)

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()