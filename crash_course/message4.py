# Crash Course
# Chapter 8 - Functions
# Exercise 8-11. Archived Messages: 
# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a 
# copy of the list of messages. After calling 
# the function, print both of your lists to show 
# that the original list has retained its messages.

def send_messages(messages, archived_messages):
    """print a message from a list of messages"""
    while messages_list:
        message = messages_list.pop()
        print(f"For the World: {message}")
        archived_messages.append(message)


def arch_messages(archived_messages):
    """Show the messages that were archived."""
    print("\nThe following messages have been archived:")
    for archived_message in archived_messages:
        print(archived_message)


messages_list = ['The world is not flat!', 'Donald Trump is a bad President!', 'COVID-19 will only go away when we find a vaccine!',
            'The world, and humanity will survive this virus too...!', 'Remember, the world is not flat, and the virus may have started in China, but it could have started anywhere!']
archived_messages = []

send_messages(messages_list[:], archived_messages)

arch_messages(archived_messages)

print("\nThese are the original messages:")
print(messages_list)
