# Try It Yourself Exercise - Pg.42
# 3-5 Changing The Guest List
guest_list = ['roger federer', 'aaron finch', 'alex honnold']
invite_0 = f"Dear {guest_list[0].title()},\nYou are cordially invited to attend a dinner party"
invite_1 = f"Dear {guest_list[1].title()},\nYou are cordially invited to attend a dinner party"
invite_2 = f"Dear {guest_list[2].title()},\nYou are cordially invited to attend a dinner party"
print(invite_0)
print(invite_1)
print(invite_2)
declined_invitation = 'alex honnold'
guest_list.remove(declined_invitation)
guest_list.append('hayley williams')
print(guest_list)
print(f"\n{invite_0}")
# print(invite_1)
print(invite_2)
# print(f"\nUnfortunately, {declined_invitation.title()}, is unable to attend.")