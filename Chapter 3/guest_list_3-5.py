# Try It Yourself Exercise - Pg.42
# 3-5 Changing The Guest List
guest_list = ['roger federer', 'aaron finch', 'alex honnold']
print("Original Invitations:")
print(f"Dear {guest_list[0].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[1].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[2].title()},\nYou are cordially invited to attend a dinner party")
declined_invitation = 'aaron finch'
guest_list.remove(declined_invitation)
guest_list.append('hayley williams')
print("New Invitations Sent:")
print(f"Dear {guest_list[0].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[1].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[2].title()},\nYou are cordially invited to attend a dinner party")
print("Apologies:")
print(f"Unfortunately, {declined_invitation.title()}, is no longer able to attend.")