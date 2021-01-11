# Try It Yourself Exercise - Pg.193
# 10-5 Programming Poll
########################################################################################################################
# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores all the responses
########################################################################################################################

filename = 'programming_poll_responses.txt'

while True:
    programming_poll = input("Please tell us a reason you enjoy programming. (Type 'exit' to quit): ")
    if programming_poll == 'exit':
        break
    else:
        with open (filename, 'a') as file_object:
            print(f"Thank you for submitting your response.")
            file_object.write(f"{programming_poll}\n")