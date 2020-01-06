# Try It Yourself Exercise - Pg.25
# 2-3 Use a variable for a name and print a message
print("Exercise 2-3")
person_name = "carlos"
message = f"Ciao Bella {person_name}, how good's the cricket?"
print(message)

# 2-4 Name Cases Use a variable for a name and print it in lowercase, uppercase and title case
# I have made the r and cap to highlight that it is working as intended
print("Exercise 2-4")
person_name = "saRah"
print(person_name)
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

# 2-5 Famous quote. Print a quote and name of author
print("Exercise 2-5")
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# 2-6 Represent the famous person using a variable and create a variable called message. Print the message
# I added an extra step and made the quote itself a variable and strung them together
print("Exercise 2-6")
famous_person = "Albert Einstein"
quote = '"A person who never made a mistake never tried anything new."'
message = f'{famous_person} once said, {quote}'
print(message)

# 2-7 Stripping names from beginning and end of the name
# Stripped requested white spaces and also added a secondary function to last print out and fixed the (ZZ's) in name
print("Exercise 2-7")
name = "  jaZZa  "
show = f"\t{name}\n\t{name.lstrip()}\n\t{name.rstrip()}\n\t{name.strip()}\n\t{name.strip().title()}"
print(show)