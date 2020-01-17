# Try It Yourself Exercise - Pg 36
# 3-1 Store names of people in a list and print each persons name individually
print("Exercise 3-1")
names = ['carl', 'dave', 'emily', 'shreya', 'ainslee']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

# 3-2 Create a message and that is then printed and personalised with each of the above names
print("Exercise 3-2")
message = "is an amazing and adorable human being!"
print(f'{names[0].title()} {message}')
print(f'{names[1].title()} {message}')
print(f'{names[2].title()} {message}')
print(f'{names[3].title()} {message}')
print(f'{names[4].title()} {message}')

# 3-3 Make a personal list about transportation and print a series of statements about these items
print("Exercise 3-3")
transportation_modes = ['car', 'lancer', 'stinger', 'wrx', '86']
transportation_brands = ['mitsubishi', 'toyota', 'kia', 'subaru']
print(f'My preferred transportation mode is by {transportation_modes[0]}')
print(f'I currently drive a {transportation_brands[0].title()} {transportation_modes[1].title()}')
print(f'The {transportation_brands[2].capitalize()} {transportation_modes[2].title()} looks sexy but is a bit pricey')
print(f'The {transportation_brands[3].title()} {transportation_modes[3].capitalize()} looks good, but not as fast and a bit pricey')
print(f'The {transportation_brands[1].title()} {transportation_modes[4]} looks good, good price, but where is the TURBO?')
