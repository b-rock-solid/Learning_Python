# Stripping white space is generally done in the real world to clean up user input
# before it's stored inside of program
# Removing white space from the right of a string/value using rstrip
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
# Removing white space from the left of a string/value using lstrip
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())
# Removing white space from both left/right sides of a string/value using strip
favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip())