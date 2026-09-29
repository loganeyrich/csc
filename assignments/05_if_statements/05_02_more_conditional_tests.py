'''
Logan Eyrich
Chapter 5
More Conditional Tests
'''

# Creates a variable called computer and assigns it the value 'dell'
computer = 'dell'
# Prints a statement predicting the result of the conditional test
print("Is computer == 'dell'? I predict True.")
print(computer == 'dell')
print("\nIs computer == 'asus'? I predict False.")
print(computer == 'asus')

# Creates a true and false string inequality
print("computer" == "dell")
print("computer" == "asus")

# Tests for equality and inequality with strings
equality = 'same'
inequality = 'different'
print("\nIs inequality != equality? I predict False.")
print(inequality != equality)
print("\nIs inequality == equality? I predict True.")

# Tests using the lower() method
user_input = 'Dell'
print("\nIs user_input.lower() == 'dell'? I predict True.")
print(user_input.lower() == 'dell')
print("\nIs user_input.lower() == 'Dell'? I predict False.")
print(user_input.lower() == 'Dell')

# Numerical tests involving equality/inequality, greater than and less than, greater than or equal to, and less than or equal to
ram = 16
print("\nIs ram == 16? I predict True.")
print(ram == 16)
print("\nIs ram != 16? I predict False.")
print(ram != 16)
print("\nIs ram > 8? I predict True.")
print(ram > 8)
print("\nIs ram < 8? I predict False.")
print(ram < 8)
print("\nIs ram >= 16? I predict True.")
print(ram >= 16)
print("\nIs ram <= 8? I predict False.")
print(ram <= 8)

# Tests using the and keyword and the or keyword
storage = 512
print("\nIs ram == 16 and storage == 512? I predict True.")
print(ram == 16 and storage == 512)
print("\nIs ram == 16 and storage == 256? I predict False.")
print(ram == 16 and storage == 256)
print("\nIs ram == 8 or storage == 512? I predict True.")
print(ram == 8 or storage == 512)
print("\nIs ram == 8 or storage == 256? I predict False.")
print(ram == 8 or storage == 256)

# Test whether an item is in a list
brands = ['dell', 'hp', 'lenovo']
print("\nIs 'hp' in brands? I predict True.")
print('hp' in brands)
print("\nIs 'apple' in brands? I predict False.")
print('apple' in brands)

# Test whether an item is not in a list
print("\nIs 'macbook' not in brands? I predict True.")
print('macbook' not in brands)
print("\nIs 'dell' not in brands? I predict False.")
print('dell' not in brands)