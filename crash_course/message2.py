# Crash Course
# Chapter 8 - Functions
# Exercise 8-9. Messages: Make a list containing 
# a series of short text messages. Pass the list 
# to a function called show_messages(), which 
# prints each text message.

messages = ['The world is not flat!', 'Donald Trump is a bad President!', 'COVID-19 will only go away when we find a vaccine!', 'The world, and humans will survive this virus too...!', 'Remember, the world is not flat, and the virus may have started in China, but it could have started anywhere!']

def show_message(message):
    for message in messages:
        print(message)

show_message(messages)
