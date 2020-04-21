########################################################################################################################
#                                                   Using A Flag                                                       #
########################################################################################################################
# In parrot.py we had a program perform certain tasks while a given condition was true
# In more complicated programs, many different events could cause the program to stop running
# For a program that should run only as long as many conditions are true
# You can define one variable that determines whether or not the entire program is active
# This variable is called a 'flag'

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)