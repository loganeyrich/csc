'''
Logan Eyrich
Chapter 9
Difficulty: 8/10
'''

# I couldn't figure this one out it was difficult
from 09_08_privileges import Admin

self = Admin('Logan', 'Eyrich', 'logan@example.com')
self.describe_user()
self_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
self.privileges.privileges = self_privileges
self.privileges.show_privileges()