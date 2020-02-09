# Try It Yourself Exercise - Pg.46
# 3-9 Use len() to print number of guests attending
guest_list = ['roger federer', 'aaron finch', 'alex honnold']
invite_0 = f"Dear {guest_list[0].title()},\nYou are cordially invited to attend a dinner party"
invite_1 = f"Dear {guest_list[1].title()},\nYou are cordially invited to attend a dinner party"
invite_2 = f"Dear {guest_list[2].title()},\nYou are cordially invited to attend a dinner party"
print(invite_0)
print(invite_1)
print(invite_2)
print(f"\nThe number of guests attending the dinner is currently:\n{len(guest_list)}")