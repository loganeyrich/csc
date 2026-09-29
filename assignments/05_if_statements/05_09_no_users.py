'''
Logan Eyrich
Chapter 5
No Users
'''

# Creates an empty list for the usernames and because there is no username string bvalue it skips the for loop, and if & else conditions inside which prints the else outside as none of the conditions were met.
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")