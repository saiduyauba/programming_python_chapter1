
#List of places (not in alphabetical order)
places = ["madina", "algeria", "paris", "dubai", "istanbul"]

#Original order
print("Original list:")
print(places)

#Alphabetical order (without changing the list)
print("\nSorted (alphabetical):")
print(sorted(places))

#Original list again
print("\nOriginal list after sorted():")
print(places)

#Reverse alphabetical order (without changing the list)
print("\nSorted (reverse alphabetical):")
print(sorted(places, reverse=True))

#Original list again
print("\nOriginal list after reverse sorted():")
print(places)

#Reverse the list (modifies the list)
places.reverse()
print("\nList after reverse():")
print(places)

#Reverse again to restore original order
places.reverse()
print("\nList after second reverse():")
print(places)

#Sort the list alphabetically (modifies the list)
places.sort()
print("\nList after sort():")
print(places)

#Sort in reverse-alphabetical order (modifies the list)
places.sort(reverse=True)
print("\nList after reverse sort():")
print(places)