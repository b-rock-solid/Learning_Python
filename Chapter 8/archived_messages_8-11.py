# Try It Yourself Exercise - Pg.146
# 8-11 Archived Messages
########################################################################################################################
# Start with your program from exercise 8-10
# Call the function send_messages() with a copy of the list of messages
# After calling the function, print both lists to show the original list has retained its messages
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

send_messages(unsent_messages[:], sent_messages)
show_messages(sent_messages)

print(f"\nOriginal unsent messages list: \n{unsent_messages}")