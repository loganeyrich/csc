'''
Logan Eyrich
Chapter 9
Difficulty: 3/10
'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

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