'''
Logan Eyrich
Chapter 5
Hello Admin
'''

# Creates a list of five usernames, including admin
usernames = ['Drew', 'Alex', 'Admin', 'Evan', 'Chris']

# Loops through the list to print a greeting for each different username
for username in usernames:
    if username.lower() == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in.")
