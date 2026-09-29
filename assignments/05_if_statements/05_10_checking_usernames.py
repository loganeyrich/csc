'''
Logan Eyrich
Chapter 5
Checking Usernames
'''

# List of current users
current_users = ['Alex', 'Evan', 'admin', 'Drew', 'John']

# Make a copy of current_users containing the lowercase versions of all existing users
current_users_lower = [user.lower() for user in current_users]

# List of new users, with some overlap and different casing
new_users = ['logan', 'WILLIE', 'angel', 'JOHN', 'Nick']

# Loop through new_users to check if each username is already used
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. You will need to enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
