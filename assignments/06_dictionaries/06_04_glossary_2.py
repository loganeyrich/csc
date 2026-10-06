'''
Logan Eyrich
Chapter 6 
Glossary 2
'''
#Creates a dictionary containing programming terms and their definitions.
glossary = {'Variable' : 'A named location used to store data in the memory.',
            'String' : 'A sequence of characters.',
            'List' : 'A collection of items in a particular order.',
            'Dictionary' : 'A collection of key-value pairs.',
            'Syntax' : 'The set of rules that defines the combinations of symbols that are considered to be correctly structured programs in that language.'
            }
# Creates a for loop to print each term and its definition in the glossary dictionary.
for term, definition in glossary.items():
    print(f"{term}: {definition}\n")


