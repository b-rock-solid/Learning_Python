# Try It Yourself Exercise - Pg.105
# 6-6 Polling
########################################################################################################################
# Use the code in favourite_language.py
# Make a list of people who should take the poll
# Include some names that are already in the dictionary and some that are not
# Loop through the list of people who should take the poll
# If they have taken the poll, print a message thanking them for responding
# If they haven't, print a message asking them complete the poll
########################################################################################################################
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['Jen', 'saRaH', 'cArl', 'BrOcK', 'daVe', 'phil']

for person in people:
    if person.lower() in favourite_languages.keys():
        print(f"Thank you {person.title()} for completing our poll :-)")
    else:
        print(f"Hi {person.title()}, could you please take our poll?")


# I also added another CaSe check in the if statement
# By adding the person.lower() in the if statement, it doesn't matter what is in the people list