# Using get() to Access Values
# You can use the get function to set a default value that will be returned if the requested key doesn't exist
# The get() argument requires a key as a first argument
# As a second optional argument, you can pass the value to be returned if the key doesn't exist

alien_0 = {'colour': 'green', 'speed': 'slow'}
# print(alien_0['points'])
# If you try and print alien_0 referencing the 'points' key which doesn't exist, you will get an error
# You can mitigate this by using the get() command

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If there's a chance the key you're asking for might not exist, consider using the get() method