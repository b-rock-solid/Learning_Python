########################################################################################################################
#                                          Making an Argument Optional                                                 #
########################################################################################################################

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# First and last name
musician = get_formatted_name('jimi','hendrix')
print(musician)

# First, middle and last name
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)