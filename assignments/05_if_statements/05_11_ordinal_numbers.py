'''
Logan Eyrich
Chapter 5
Ordinal Numbers
'''

# Creates a list for the variable 'numbers' that stores integer values 1 to 9
numbers = [1,2,3,4,5,6,7,8,9]
# The loop goes through each number one by one
# For the if-elif-else chain it checks if the number is 1,2,or 3 to print 1st,2nd,and 3rd.
# Every other number falls into the else condition which uses the stem of the number and adds 'th' to the end of it.
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")