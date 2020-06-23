# Try It Yourself Exercise - Pg.146
# 8-9 Messages
########################################################################################################################
# Make a list containing a series of short text messages
# Pass the list to a function called show_messages(), which prints each text message
########################################################################################################################

def show_messages(text_message):
    """Shows all text messages within a list."""
    for message in text_message:
        print(message)

messages = ["Hi, how are you?", "Sorry, can't talk now :(", "ttyl", "ttfn", "lol"]

show_messages(messages)