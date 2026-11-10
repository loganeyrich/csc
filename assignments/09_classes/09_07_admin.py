'''
Logan Eyrich
Chapter 9
Difficulty: 6/10
'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
user_1 = User("Logan", "Eyrich")
user_2 = User("Paul", "Chen")
user_3 = User("David", "Martinez")

describe_users = [user_1, user_2, user_3]
greet_users = [user_1, user_2, user_3]

for user in describe_users:
    user.describe_user()

for user in greet_users:
    user.greet_user()

admin_1 = Admin("Logan", "Eyrich")
admin_1.show_privileges()