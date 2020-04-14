# Try It Yourself Exercise - Pg.117
# 7-3 Multiples of Ten
########################################################################################################################
# Ask a user for a number, and then report whether the number is a multiple of 10 or not
########################################################################################################################

number = input("Give me a number and I'll tell you if it's a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10")
else:
    print(f"The number {number} is not a multiple of 10")