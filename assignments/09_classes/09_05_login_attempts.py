'''
Logan Eyrich
Chapter 9
Difficulty: 6/10
'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

user_1 = User("Logan", "Eyrich")
user_2 = User("Paul", "Chen")
user_3 = User("David", "Martinez")

describe_users = [user_1, user_2, user_3]
greet_users = [user_1, user_2, user_3]

for user in describe_users:
    user.describe_user()

for user in greet_users:
    user.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Login attempts after reset: {user_1.login_attempts}")