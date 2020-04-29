########################################################################################################################
#                                      Passing Information to a Function                                               #
########################################################################################################################

# By adding 'username' in the parentheses, you allow the function to accept any value of 'username' you specify.
# Below we are passing he 'username' info with 'jesse'
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')