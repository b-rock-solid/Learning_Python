# Try It Yourself Exercise - Pg.127
# 7-8 Deli
########################################################################################################################
# Make a list called sandwich_orders and fill it with names of sandwiches
# Loop through the list of sandwich orders and print a message for each order
# As each sandwich is made, move it to a list of finished sandwiches
# After all sandwiches have been made, print a message listing each sandwich that was made
########################################################################################################################

sandwich_orders = ['tuna', 'club', 'meatball', 'roast beef', 'turkey']

finished_orders = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I've finished making your {current_sandwich.title()} Sandwich.")
    finished_orders.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_orders:
    print(sandwich.title())