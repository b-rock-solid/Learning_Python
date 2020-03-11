# Try It Yourself Exercise - Pg.85
# 5-6 Stages of Life
########################################################################################################################
# Write an if-elif-else chain that determines a person's stage of life
# If age is less than 2, print message the person is a baby
# If age is at least 2 but less than 4, print they are a toddler
# If age is at least 4 but less than 13, print they are a kid
# If age is at least 13 but less than 20, print they are a teenager
# If age is at least 20 but less than 65, print they are an adult
# If age is 65 or older, print they are an elder
########################################################################################################################
# sol = stage of life

age = 16

if age < 2:
    sol = 'baby'
elif age < 4:
    sol = 'toddler'
elif age < 13:
    sol = 'kid'
elif age < 20:
    sol = 'teenager'
elif age < 65:
    sol = 'adult'
elif age >= 65:
    sol = 'elder'

print(f"Your current stage of life is {sol.title()}.")