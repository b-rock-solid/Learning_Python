# Try It Yourself Exercise - Pg.117
# 7-2 Restaurant Seating
########################################################################################################################
# Write a program that asks the user how many people are in their dinner group
# If the answer is more than eight, print a message saying they'll have to wait for a table
# Otherwise, report that their table is ready
########################################################################################################################

group_size = input("How many guests will be eating with us tonight? ")
group_size = int(group_size)

if group_size > 8:
    print(f"\nWith a group size of {group_size}, please kindly wait in the bar while we get your table ready.")
else:
    print(f"\nYour table for {group_size} is ready, please follow your waiter to your seat.")