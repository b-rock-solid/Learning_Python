# Evaluating multiple conditions using 'if-elif-else' syntax
########################################################################################################################
# Possible real world situation:
# Amusement park charges different rates for different age groups:
# Admission is free under age 4
# Admission between ages 4 and 18 is $25
# Admission 18 or older is $40
########################################################################################################################
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# A more efficient way to write the above code:

age = 25

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print (f"Your admission cost is ${price}.")

# Introducing another elif block:
# Amusement park introduces a seniors discount for ages 65 and over for $20

age = 72

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print (f"Your admission cost is ${price}.")

# You're also able to omit the "else" block completely.
# Sometimes it is clearer to use an additional "elif" statement

age = 65

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print (f"Your admission cost is ${price}.")