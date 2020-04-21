# Try It Yourself Exercise - Pg.127
# 7-9 No Pastrami
########################################################################################################################
# Using the list sandwich_orders from exercise 7-8, make sure pastrami appears in the list at least 3 times
# Add code near the beginning to print a message saying the deli has run out of pastrami
# Use a while loop to remove all occurrences of pastrami from sandwich_orders
# Make sure no pastrami sandwiches end up in finished_sandwiches
########################################################################################################################

sandwich_orders = ['pastrami', 'tuna', 'club', 'pastrami', 'meatball', 'roast beef', 'pastrami', 'turkey', 'pastrami']

finished_orders = []

print("Unfortunately the deli has run out of pastrami, we apologize for any inconvenience.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I've finished making your {current_sandwich.title()} Sandwich.")
    finished_orders.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_orders:
    print(sandwich.title())