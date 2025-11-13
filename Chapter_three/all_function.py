#Create a list of cities
cities = ["lagos", "cairo", "nairobi", "istanbul", "tokyo"]

#Print original list
print("Original list:")
print(cities)

#Append a city
cities.append("paris")
print("\nAfter append:")
print(cities)

#Insert a city at position 2
cities.insert(2, "makkah")
print("\nAfter insert at index 2:")
print(cities)

#Delete a city by index
del cities[1]
print("\nAfter deleting index 1:")
print(cities)

#Remove a city by name
cities.remove("tokyo")
print("\nAfter removing 'Tokyo':")
print(cities)

#Pop the last item
last_city = cities.pop()
print("\nAfter pop():")
print(cities)
print("Popped city:", last_city)

#Sort the list permanently
cities.sort()
print("\nAfter sort():")
print(cities)

#Sort in reverse order
cities.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(cities)

#Temporarily sort with sorted()
print("\nUsing sorted():")
print(sorted(cities))

#Reverse the list
cities.reverse()
print("\nAfter reverse():")
print(cities)

#Length of list
print("\nTotal number of cities:", len(cities))
