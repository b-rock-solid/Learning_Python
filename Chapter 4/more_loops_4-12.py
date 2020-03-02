# Try It Yourself Exercise - Pg.65
# 4-12 More Loops
# Write 2 for loops to print each list of foods from the original foods.py program
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend's favourite foods are:")
for fr_foods in friend_foods:
    print(fr_foods.title())