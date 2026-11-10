'''
Logan Eyrich
Chapter 9
Difficulty: 6/10
'''

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
class Admin:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.privileges = Privileges()
    def describe_user(self):
        print(f"Admin Username: {self.username}")
        print(f"Admin Email: {self.email}")

admin = Admin("Logan Eyrich", "logan@example.com")
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_privileges()
