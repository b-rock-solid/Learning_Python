# Slicing a list
# To make a slice, specify the index of the first and last elements you want to work with
# Same as the range() function, Python stops one item before the second index you specify
# To output the first three elements in a list, you would request indicies 0 through 3
# This would return the elements 0, 1 and 2
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"Players List:\n{players}")
print("\nIndex starting at 0:")
print(players[0:3])
# You can generate any subset of the list. If you want the 2nd, 3rd and 4th index, start at index 1 and end at 4
print(f"\nIndex starting at 1:")
print(players[1:4])
# You can omit the first index, and it will automatically start at the beginning of the list
print(f"\nOmitting the first index:")
print(players[:4])
# The same can be applied to the end of the list. List where you wish to start from and Python will go till the end
print(f"\nOmitting the second index:")
print(players[2:])
# If we wanted to output the last three players on the roster, we can use the following:
print(f"\nLast three players on roster:")
print(players[-3:])
# NOTE: You can include a third value in the brackets indicating a slice.
# If a thrid value is included, this tells Python how many items to skip between items in the specified range

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())