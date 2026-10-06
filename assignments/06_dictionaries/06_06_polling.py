'''
Logan Eyrich
Chapter 6
Polling
'''
# Creates a dictionary of favorite languages
favorite_languages = {
'Jen': 'Python',
'Sarah': 'C++',
'Edward': 'Rust',
'Phil': 'Python',
'Logan': 'Java',
'Drew': 'JavaScript'
 }
# People who should take the poll
people_to_poll = ['Jen', 'Sarah', 'Michael', 'Logan', 'John']

# Thank people who have responded and invite everyone else
for person in people_to_poll:
	if person in favorite_languages:
		print(f"Thank you, {person}, for responding to the poll.")
	else:
		print(f"{person}, please take the favorite languages poll.")