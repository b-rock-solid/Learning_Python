########################################################################################################################
#                                   Letting the User Choose When to Quit                                               #
########################################################################################################################
# We can make the parrot.py program run as long as the user wants by putting most of the program inside a 'while' loop
# We'll define a 'quit value', then keep the program running as long as that value is not entered

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
# Adding this if test so the word 'quit' isn't printed when exiting the program
    if message != 'quit':
        print(message)