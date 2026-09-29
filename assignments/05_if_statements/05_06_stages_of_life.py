'''
Logan Eyrich
Chapter 5
Stages of Life
'''

# Creates a variable age and sets it to 21. Then determines based on the range it belongs into to determine the stage of life the person is in.
# Then prints accordingly to which range, in this case since it's in between 20 and 65 range you are an adult, which is what the if-elif-else chain prints.
age = 21
if(age < 2):
    print("You are a baby")
elif(age < 4):
    print("You are a toddler")
elif(age < 13):
    print("You are a kid")
elif(age < 20): 
    print("You are a teenager")
elif(age < 65):
    print("You are an adult")
else:
    print("You are an elder")