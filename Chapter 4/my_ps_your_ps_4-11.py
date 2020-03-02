# Try It Yourself Exercise - Pg.65
# 4-11 My Pizzas, Your Pizzas
# Make a copy of the list of pizzas and call it friend_pizzas
# Add a new pizza to the original list, add a different one to the list friend_pizzas
# Prove they are seperate by printing the lists
pizzas = ['pepperoni', 'godfather', 'vegorama']
friend_pizzas = pizzas[:]

pizzas.append('garlic pizza')
friend_pizzas.append('meatlovers')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())