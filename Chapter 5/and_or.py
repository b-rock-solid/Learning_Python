# Using the 'and' and 'or' conditional tests

# Check if two people are both over 21 using 'and'
age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >= 21:
    print("First ages = True")
else:
    print("First ages = False")

age_1 = 21

if age_0 >= 21 and age_1 >= 21:
    print("Second ages = True")
else:
    print("Second ages = False")


# Check if one of the 2 people is over 21 using 'or'
age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21:
    print("One of you is 21 or older!")
else:
    print("Neither of you is over 21, GET OUT!")

age_0 =19

if age_0 >= 21 or age_1 >= 21:
    print("One of you is 21 or older!")
else:
    print("Neither of you is 21 or older, GET OUT!")