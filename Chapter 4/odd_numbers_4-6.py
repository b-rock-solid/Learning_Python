# Try It Yourself Exercise - Pg.60
# 4-6 Odd Numbers
# Use the third argument of the range() function to make a list of the odd numbers from 1 - 20
odd_numbers = []
for value in range(1, 21, 2):
    odd_numbers.append(value)
    print(odd_numbers[-1])

# Created blank list
# Created for loop with a range of 1 - 20(21), adding 2 each time
# Append to the list the result of adding 2
# Print the last thing added to the list with the [-1]
# Result is list of odd numbers from 1 - 20 printed individually