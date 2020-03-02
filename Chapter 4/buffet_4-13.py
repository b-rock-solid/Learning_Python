# Try It Yourself Exercise - Pg.68
# 4-13 Buffet
# Store five simple foods in a tuple
# For loop the tuple
# Re-define the list by replacing 2 of the items and re-printing the tuple

buffet = ('roast pork', 'roast beef', 'roast veggies', 'potato bake', 'salad')
print("Food served at the buffet are:")
for food in buffet:
    print(food.title())

print("\nThe new buffet menu is:")
buffet = ('roast pork', 'roast chicken', 'roast veggies', 'potato bake', 'peas and corn')
for food in buffet:
    print(food.title())