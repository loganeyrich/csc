from admin import Admin

self = Admin('Logan', 'Eyrich', 'logan@example.com')
self.describe_user()

self_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
self.privileges.privileges = self_privileges]
print(f"\nThe admin {self.username} has these privileges: ")
self.privileges.show_privileges()