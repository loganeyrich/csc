'''
Logan Eyrich
Chapter 8
Difficulty: 5/10
'''

def build_profile(first_name, last_name, **user_info):
	profile = {
		'first_name': first_name,
		'last_name': last_name,
	}
	profile.update(user_info)
	return profile

user_profile = build_profile(
	'Logan',
	'Eyrich',
	location='Reading',
	field='Cybersecurity',
	hobby='Gaming',
)
print(user_profile)  