guest_lists = ['abbas', 'sultan', 'umar']
for guest in guest_lists:
    print(f"Mr {guest.title()}, you are invited to my dinner.")
print(f"\nSorry! Mr {guest_lists[0]} can't make the dinner.")
print(f"Guest Lists length is {len(guest_lists)}.\n")

#modifying the guest lists
guest_lists[0] = 'abubakar'
for new_guest in guest_lists:
    print(f"Mr {new_guest.title()}, you are invited to my dinner.")
print("\nThank you all for accepting the invitation.")

# I found a bigger dinner table, so now more space is available
print("\nI found a bigger dinner table, so more space is available.")
guest_lists.insert(0, 'muhd')
guest_lists.insert(2, 'sadiq')
guest_lists.append('bello')
for guest in guest_lists:
    print(f"Mr {guest.title()}, you are invited to my dinner.")
print(f"\nThank you for Coming.")

#printing the length of the list
print(f"Guest Lists length is {len(guest_lists)}.\n")

#The new bigger dinner table may not be available at time, the available is for two person.
print("\nSorry, i can invite only two people.\n")
first_pop = guest_lists.pop()
print(f"Sorry, {first_pop.title()} i can't invite you to the dinner.")
second_pop = guest_lists.pop()
print(f"Sorry, {second_pop.title()} i can't invite you to the dinner.")
third_pop = guest_lists.pop()
print(f"Sorry, {third_pop.title()} i can't invite you to the dinner.")
forth_pop = guest_lists.pop()
print(f"Sorry, {forth_pop.title()} i can't invite you to the dinner.\n")
print(f"Guest Lists length is {len(guest_lists)}.\n")
for remain_guest in guest_lists:
    print(f"Mr {remain_guest.title()}, you are still invited to my dinner.")
del guest_lists[ 0:]
print(guest_lists)
print(f"Guest Lists length is {len(guest_lists)}.\n")