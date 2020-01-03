# Variables to be used
first_name = "ada"
last_name = "lovelace"
# f strings format strings by replacing the name of any variable in braces with its value
full_name = f"{first_name} {last_name}"
# Prints to console the full_name string as is
print(full_name)
# Prints to console the full_name string using the title method to capatilise the first letter of each word
print(full_name.title())
# Prints to console a custom message along with the full_name string
print(f"Hello, {full_name.title()}!")
# f-string used to compose a message, which is assigned to the variable "message". Message is then printed to console
message = f"Welcome! Your name is {full_name.title()}"
print(message)