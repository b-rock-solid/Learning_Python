# Try It Yourself Exercise - Pg.42
# 3-7 Shrinking The Guest List
guest_list = ['roger federer', 'aaron finch', 'alex honnold']
print("Original Invitations:")
print(f"Dear {guest_list[0].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[1].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[2].title()},\nYou are cordially invited to attend a dinner party")
declined_invitation = 'aaron finch'
guest_list.remove(declined_invitation)
guest_list.append('hayley williams')
guest_list.insert(0, 'novak djokovic')
guest_list.insert(2, 'caroline wozniacki')
guest_list.append('adam scott')
print("New Invitations Sent:")
print(f"Dear {guest_list[0].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[1].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[2].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[3].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[4].title()},\nYou are cordially invited to attend a dinner party")
print(f"Dear {guest_list[5].title()},\nYou are cordially invited to attend a dinner party")
# Print any declined invitations
print("Apologies:")
print(f"Unfortunately, {declined_invitation.title()}, is no longer able to attend.")
# Printing the current list of guests after initial manipulation of data
print(f"Current List of Guests:\n{guest_list}")
print("Unfortunately, the only table available will only be able to fit 2 guests :(")
print("Guest Removals:")
guest_cut_1 = guest_list.pop()
print(f"Dear {guest_cut_1.title()},\nI will no longer be able to have you around for dinner due to catering difficulties.\nHope to catch up with you soon!")
guest_cut_2 = guest_list.pop(3)
print(f"Dear {guest_cut_2.title()},\nI will no longer be able to have you around for dinner due to catering difficulties.\nHope to catch up with you soon!")
guest_cut_3 = guest_list.pop(0)
print(f"Dear {guest_cut_3.title()},\nI will no longer be able to have you around for dinner due to catering difficulties.\nHope to catch up with you soon!")
guest_cut_4 = guest_list.pop()
print(f"Dear {guest_cut_4.title()},\nI will no longer be able to have you around for dinner due to catering difficulties.\nHope to catch up with you soon!")
print("2 Invited Guests:")
print(f"Dear {guest_list[0].title()},\nYou are still invited to attend my dinner party")
print(f"Dear {guest_list[1].title()},\nYou are still invited to attend my dinner party")
# Making the list empty
del guest_list[0]
del guest_list[0]
print(f"Printout of Empty Guest List:\n{guest_list}")