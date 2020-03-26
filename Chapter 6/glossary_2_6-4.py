# Try It Yourself Exercise - Pg.105
# 6-4 Glossary 2
########################################################################################################################
# Use the code from the previous glossary exercise and clean it up using loops within the dictionary
# Once the loop is working, add 5 more terms and meanings to the glossary and ensure it is working
########################################################################################################################

glossary = {
    'lists': 'A list is a collection of items in a particular order.'
            '\nA list in Python is indicated with square brackets [].',
    'strings': 'A string is a series of characters. Anything inside quotes is considered a string in Python.'
               '\nYou can use either single or double quotes to form a string.',
    'comments': 'A comment allows you to write notes in English within your programs.'
                '\nIn Python, the hash (#) indicates a comment.',
    'pop': 'The pop() method is used to remove the last item off of a list.'
           '\nThis method is useful as it allows you to use the item after removing it.',
    'loop': 'Looping allows you to take the same action, or set of actions, with every item in a list.'
            '\nThis allows you to work efficiently with lists of any length.',
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.'
                  '\nEach key is connected to a value. The value can be any object you can create in Python!',
    'if statements': 'There are several different types of if statements you can use, and each are used'
                     '\nin different situations. If the test is equates to TRUE, the statement is run,'
                     '\notherwise, the it evaluates to FALSE and ignores the code following the if statement.',
}

for term, definition in glossary.items():
    print(f"\nThe definition for '{term}' is:\n{definition}.")