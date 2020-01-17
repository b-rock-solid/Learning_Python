# A list is a collection of items in a particular order
# In Python, square brackets ([]) indicate a list, with individual elements seperated by commas
print("Printout of whole list:")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# You can access any element in a list by telling i the position, or index of the item enclosed in square brackets
print("Printout of index 0:")
print(bicycles[0])
print("Printout of index 0 adding the title method:")
print(bicycles[0].title())

# Index positions start at '0' not '1'!
# You can access the last item in a list by using the index -1
# You can also access the last items of the list by using the negative indexes -2, -3 etc
# -2 would give second item from the end of the list -3 would be third and so forth
print("Accessing last index using -1:")
print(bicycles[-1])
print("Accessing second last index using -2:")
print(bicycles[-2])

# Using f-strings to create a message based on a value from a list
message = f'My first bike was a {bicycles[2].title()}.'
print(message)