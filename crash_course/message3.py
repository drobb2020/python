# Crash Course
# Chapter 8 - Functions
# Exercise 8-10. Sending Messages: Start with 
# a copy of your program from Exercise 8-9. 
# Write a function called send_messages() 
# that prints each text message and moves 
# each message to a new list called sent_messages 
# as it’s printed. After calling the function, 
# print both of your lists to make sure the 
# messages were moved correctly.

def send_messages(messages_list, sent_messages_list):
    """
    print a message from a list of messages

    Args:
        message (list): a custom message in a list
    """
    while messages_list:
        current_message = messages_list.pop()
        print(f"{current_message}")
        sent_messages_list.append(current_message)


def sent_messages(sent_messages_list):
    """Show the messages that were sent."""
    print("\nThe following messages were sent:")
    for sent_message in sent_messages_list:
        print(sent_message)


messages_list = ['The world is not flat!', 'Donald Trump is a bad President!', 'COVID-19 will only go away when we find a vaccine!',
            'The world, and humanity will survive this virus too...!', 'Remember, the world is not flat, and the virus may have started in China, but it could have started anywhere!']
sent_messages_list = []

send_messages(messages_list, sent_messages_list)

sent_messages(sent_messages_list)
