'''
Logan Eyrich
Code Jam
Difficulty:
'''

import matplotlib.pyplot as plt

# --- Part 1: Plotting the first 5 cubic numbers ---
x_values_5 = [1, 2, 3, 4, 5]
cubes_5 = [x**3 for x in x_values_5]

fig, ax = plt.subplots()
ax.scatter(x_values_5, cubes_5, s=100, color='red')

# Title and labels
ax.set_title("First Five Cubic Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of Value", fontsize=12)
ax.tick_params(axis='both', labelsize=10)

plt.show()

# --- Part 2: Plotting the first 5,000 cubic numbers ---
x_values_5000 = list(range(1, 5001))
cubes_5000 = [x**3 for x in x_values_5000]

fig, ax = plt.subplots()
# Using a small dot size (s=2) so 5,000 points don't blend into a single blob
ax.scatter(x_values_5000, cubes_5000, s=2, color='blue')

# Title and labels
ax.set_title("First 5,000 Cubic Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of Value", fontsize=12)
ax.tick_params(axis='both', labelsize=10)

# Adjust coordinate axis limits safely
ax.axis([0, 5100, 0, 5100**3])

plt.show()