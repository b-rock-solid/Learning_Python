# Try It Yourself Exercise - Pg.202
# 10-10 Common Words
########################################################################################################################
# Use the count() method to find out how many times a word or phrase appears in a text file.
# Download some pieces of text from gutenberg.org and see how many times the word 'the' appears in each text.
########################################################################################################################

def word_counter():
    """Counts how many times a word is found in a piece of text."""
    while True:
        print("Enter 'q' at anytime to exit the program.")
        filename = input("Please enter the filename you wish to search the contents of: ")
        if filename == 'q':
            break
        word_criteria = input("Please enter the word you wish to search for in the text\n"
                              "(For more accurate results, enter an empty space at the end of your search term): ")
        if word_criteria == 'q':
            break
        try:
            with open(filename, encoding='utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"Sorry, unable to find file '{filename}'.")
        else:
            count = contents.lower().count(word_criteria.lower())
            print(f"The file {filename} has the word '{word_criteria}' appears {count} times.")

word_counter()