first_name = "Alice"
last_name = "Helen"
string_concat = first_name + " " + last_name
print(len(string_concat))

# Indexing in Strings
print(first_name[0])
print(first_name[-1])

# Slicing in Strings
print(first_name[0:5:2])
print(first_name[::-1])
print(first_name[::1])

# Concatenation
place = "London"
city = "Cardiff"
print("I love " + place)
print(f"{place}\n"*3)

# String Operations
print(place.replace("L", "N"))

# Exercise
# Task 1: Create string variables
greeting = "Hello, World!"
name = "Alice"

# Task 2: Print the length of the greeting string
print(len(greeting))

# Task 3: Use indexing to print specific characters
print(greeting[0])
print(greeting[2])
print(name[-1])

# Task 4: Use slicing to print parts of strings
print(greeting[0:5])
print(name[1:3])

# Task 5: Print the greeting string in reverse
print(greeting[::-1])

# Task 6: Perform string concatenation
full_name = name + "Wonderland"
full_name_space = name + " Wonderland"
print(full_name)
print(full_name_space)

# Task 7: Use string repetition
chant = name*3
print(chant)

# Task 8: Use string methods
print(greeting.upper())
print(name.lower())
print(name.replace('l', 'x'))