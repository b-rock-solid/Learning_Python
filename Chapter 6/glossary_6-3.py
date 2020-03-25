# Try It Yourself Exercise - Pg.99
# 6-3 Glossary
########################################################################################################################
# Think of 5 programming words you've learned. Use these words as keys in your glossary
# Store their meanings as values
# Print each word and its meaning as neatly formatted output
########################################################################################################################

glossary = {
    'list': 'A list is a collection of items in a particular order.'
            '\nA list in Python is indicated with square brackets [].',
    'strings': 'A string is a series of characters. Anything inside quotes is considered a string in Python.'
               '\nYou can use either single or double quotes to form a string.',
    'comments': 'A comment allows you to write notes in English within your programs.'
                '\nIn Python, the hash (#) indicates a comment.',
    'pop': 'The pop() method is used to remove the last item off of a list.'
           '\nThis method is useful as it allows you to use the item after removing it.',
    'loop': 'Looping allows you to take the same action, or set of actions, with every item in a list.'
            '\nThis allows you to work efficiently with lists of any length.'
}

print(f"Throughout the course so far, I have learnt about Lists:\n{glossary['list']}")
print(f"\nI have also learnt about Strings:\n{glossary['strings']}")
print(f"\nComments:\n{glossary['comments']}")
print(f"\nPopping items off of a list:\n{glossary['pop']}")
print(f"\nAnd how to loop items in a list:\n{glossary['loop']}")