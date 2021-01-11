# Try It Yourself Exercise - Pg.191
# 10-2 Learning C
########################################################################################################################
# Use the replace() method to replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.
########################################################################################################################

file = 'learning_python.txt'


with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.strip()
    print(line.replace('Python', 'C'))

