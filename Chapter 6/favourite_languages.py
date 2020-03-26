# A Dictionary of Similar Objects
# You can use a dictionary to store one kind of information about many objects
# Example: a poll of people asking what their favourite programming language is

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

# Using a loop to get each person and their favourite language using the method item()
print("\nUsing a loop to get everybody's name and favourite programming language:")

for name, lang in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {lang.title()}.")

# Looping Through All the Keys in a Dictionary using the keys() method
print("\nLooping through the dictionary and printing only the names:")

for name in favourite_languages.keys():
    print(name.title())

# The default behaviour when looping dictionaries is looping the keys only
# This code would work exactly the same with the .keys() omitted:
# for name in favourite_languages:
# It's up to you whether you prefer to use the .keys() method to make your code easier to read

# Print a message to a couple of friends
# We'll loop through the dictionary as before, but when a name matches a friend, we'll display a different message.
print("\nCustom message for specific friends:")

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favourite_languages[name]
        print(f"\t{name.title()}, I see you love {language}!")

# You can use the keys() method to find out if a particular person wasn't polled
print("\nUsing keys() method to check if a person wasn't polled:")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")


# Looping Through a Dictionary's Keys in a Particular Order
# By default, looping through a dictionary, returns the items in the order they were inserted
# One way to change the order is to use the sorted() method
print("\nUsing sorted() method to loop the keys in a different order:")

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
# Sometimes, you'll only be interested in the values that a dictionary contains
# You can use the values() method to return a list of values withough any keys
print("\nUsing the values() method to return only values:")

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# Using the values() method returns all values, however doesn't take into consideration duplicates
# Use the set() method. This is a collection in which each item must be unique
print("\nUsing set() to create a unique collection:")

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())