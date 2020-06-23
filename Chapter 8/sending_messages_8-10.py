# Try It Yourself Exercise - Pg.146
# 8-10 Sending Messages
########################################################################################################################
# Start with your program from exercise 8-9
# Write a function called send_messages() that prints each text message and moves each message to a new list
# After calling the function, print both lists to ensure they were moved correctly
########################################################################################################################

def send_messages(unsent_messages, sent_messages):
    """Simulates sending text messages, and moves them to another list"""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"\nSending text message: {current_message}")
        sent_messages.append(current_message)

def show_messages(sent_messages):
    """Shows all sent text messages within a list."""
    print("\nThe following text messages have been sent:")
    for message in sent_messages:
        print(message)

unsent_messages = ["Hi, how are you?", "Sorry, can't talk now :(", "ttyl", "ttfn", "lol"]
sent_messages = []

send_messages(unsent_messages, sent_messages)
show_messages(sent_messages)