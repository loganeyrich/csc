'''
Logan Eyrich
Chapter 5
Alien Colors 3
'''

# Intiates the color green as the color, which runs the if statement and prints "You have gained 5 points"
alien_color = 'green'
if(alien_color == 'green'):
    print("You have gained 5 points")
elif(alien_color == 'yellow'):
    print("You have gained 10 points")
else:
    print("You have gained 15 points")

# Intiates the color yellow as the color, which runs the elif statement and prints "You have gained 10 points", instead
alien_color = 'yellow'
if(alien_color == 'green'):
    print("You have gained 5 points")
elif(alien_color == 'yellow'):
    print("You have gained 10 points")
else:
    print("You have gained 15 points")

# Intiates the color red as the color, which runs the else statement and prints "You have gained 15 points", instead of the other two
alien_color = 'red'
if(alien_color == 'green'):
    print("You have gained 5 points")
elif(alien_color == 'yellow'):
    print("You have gained 10 points")
else:
    print("You have gained 15 points")

