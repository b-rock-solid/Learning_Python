# Modifying Elements in a List
# You can add, remove or modify a list similar to accessing a list item
print("Original List:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying index 0 ('honda' to 'ducati)
print("Modified List:")
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending elements to a list using the append element
# Resetting motorcyles variable to the original source and printed using one line with \n and f-string
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'Reset Original List:\n{motorcycles}')
motorcycles.append('ducati')
print(f'Appended List:\n{motorcycles}')

# You can use the append call to build lists dynamically
# Reset the list to have nothing in it
motorcycles = []
print(f'Empty List:\n{motorcycles}')
# Creating the list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f'Recreated List:\n{motorcycles}')
# Appending items like this is handy as you won't often know what data users want to store in a program
# Put users in control by defining an empty list, then append each new value provided

# Inserting elements into a List by using the insert() method.
print(f'Original List:\n{motorcycles}')
# Inserting into the List
motorcycles.insert(0, 'ducati')
print(f'Inserted List:\n{motorcycles}')

# Removing elements from a List
# Removing an Item using the del Statement
# This method is used if you know the index of the item you wish to remove (E.g [0])
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'Re-print of List:\n{motorcycles}')
del motorcycles[0]
print(f'Deleted element from List:\n{motorcycles}')
# Once an item is deleted, you can no longer access the value that was removed after the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'Del statement eg2:\n{motorcycles}')
del motorcycles[1]
print(f'Delete element from List:\n{motorcycles}')

# Removing an Item Using the pop() Method
# The pop method removes the last item of a list, but allows you to work with that item after removing it
print("Removing an Item using the pop() method:")
# Create the list and print it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 'Pop' a value from the list and store it in the variable 'popped_motorcycle'
popped_motorcycle = motorcycles.pop()
# Show the removed value from 'motorcycles' list
print(motorcycles)
# Show that you still have access to the removed value which is now assigned to 'popped_motorcycle'
print(popped_motorcycle)

# Example of how the pop() method would be useful
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping items from any position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")