'''
Logan Eyrich
Chapter 8
Difficulty: 4/10
'''

messages = ['Hello', 'How are you?', 'Goodbye']
sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)