'''
Logan Eyrich
Code Jam
Difficulty: 8/10
'''

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep the program running as long as the user wants to simulate walks
while True:
    # Create a random walk with 5,000 points to simulate a pollen grain
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    
    # Replace ax.scatter() with ax.plot() and include a linewidth argument
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # Emphasize the first and last points using scatter to keep clear markers
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, zorder=2)

    # Remove the axes for a cleaner look
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break