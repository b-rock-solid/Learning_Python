# Try It Yourself Exercise - Pg.89
# 5-11 Ordinal Numbers
########################################################################################################################
# Store the numbers 1 through 9 in a list
# Loop through the list
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number
# Output should be 1st 2nd 3rd 4th etc
# Each result should be on a separate line
########################################################################################################################

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal = 'st'
    elif number == 2:
        ordinal = 'nd'
    elif number == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    print(f"{number}{ordinal}")