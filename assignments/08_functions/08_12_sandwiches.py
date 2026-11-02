'''
Logan Eyrich
Chapter 8
Difficulty: 4/10
'''

def make_sandwich(*items):
	print("I'm making a sandwich with:")
	for item in items:
		print(f"- {item}")

make_sandwich('tuna')
make_sandwich('ham', 'cheese')
make_sandwich('turkey', 'lettuce', 'tomato')