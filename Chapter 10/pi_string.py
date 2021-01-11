# Working with a File's Contents

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# When reading from a text file, Python interprets all text as a string.
# If you read a number and want to work with that value in a numerical context,
# you'll have to convert it to an integer using the int() function or,
# convert it to a float using the float() function.

# Working with Large Files: One Million Digits

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


# See if Your Birthday is Contained in Pi

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")