# Focus Learning: Python Level 1
# Python List
# Kavan Lam
# Oct 30, 2021

# You have 3 students and you want to store their ages
age1 = 8
age2 = 7
age3 = 9

# What if you had 1000 students?
# Oh no we are going to need a lot of variables (not good)
# Is there a better way?
# YES, we can use Python List

ages = [8, 7, 9, 10, 11, 7]  # This is a Python List

print(ages)
print(ages[0])  # We can use indexing to get specific numbers from the list
print(ages[3])  # The age at index 3 is 10

# Now lets actually look at the worksheet
print("----------------------------------")
pets = [3, 5, 1, 9, 0, 2]

print(pets[0])
print(pets[3])

pets[2] = 6
pets[5] = pets[5] + 3
print(pets)

print("---------------------------------")
print(len(pets))  # len = length
print(len("helloPP"))

print("----------------------------------")
# print(pets[8])  This will not work no such thing as index 8
pets = [3, 5, 1, 9, 0, 2]
print(pets[-1])  # This will give us the last number in the list


# Adding to and Deleting From Lists
print("----------------------------------")
names = ["john", "bob", "lily", "yo", "boo"]
names.append("To")
print(names)

names.pop(2)
print(names)
