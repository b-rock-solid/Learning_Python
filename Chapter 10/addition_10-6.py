# Try It Yourself Exercise - Pg.201
# 10-6 Addition
# 10-7 Addition Calculator
########################################################################################################################
# Write a program that prompts for two numbers, add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Wrap your code in a while loop so the user can continue to enter numbers even if they make a mistake.
########################################################################################################################

while True:
    print("\nTo exit the program type 'q' at anytime.")
    number_01 = input("Please enter the first number you wish to add: ")
    if number_01 == 'q':
        exit(1)
    number_02 = input("Please enter the second number you wish to add: ")
    if number_02 == 'q':
        exit(1)
    try:
        answer = float(number_01) + float(number_02)
    except ValueError:
        print("Please enter a valid number.")
    else:
        print(f"The answer is: {answer}")