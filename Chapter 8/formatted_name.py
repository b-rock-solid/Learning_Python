########################################################################################################################
#                                            Returning a Simple Value                                                  #
########################################################################################################################

# The 'return' statement takes a value from inside a function and sends it back to the line that called the function.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)