# Each time you use the input() function, include a clear, easy-to-follow prompt
# The prompt will tell the user exactly what kind of information you're looking for

# Sometimes you'll want to write a prompt that's longer than one line
# You can assign your prompt to a variable and pass that variable to the input() function

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")