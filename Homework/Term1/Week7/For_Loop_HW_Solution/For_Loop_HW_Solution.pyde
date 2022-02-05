# Python Level 1
# For Loops HW
# Kavan Lam
# Nov 11, 2021

# Question 1
"""
A for loop is one of the kinds of loops in Python. It allows you to loop over
something (string, list and etc). You can do some action for each thing in the
something that you provided.
"""

# Question 2
"""
The first issue is the x should be num
The second issue is the 0 and 10 need to swap places
"""

# Question 3
word = "Home"
for letter in word:
    print(letter * 6)

# Question 4
names = ["John", "Austin", "Dog", "Frank", "Daniel", "June", "Abby", "Catty", "Kavan"]
names.sort()
print(names)

if len(names[0]) % 2 == 0:
    print("The first student has an even number of letters")
else:
    print("The first student has an odd number of letters")

# Question 5
numbers = [23, 12, 5, 12, 45, 9, 7, 6, 1, 78, 90, 100, 71]
greater_than_50 = 0

for num in numbers:
    if num > 50:
        greater_than_50 = greater_than_50 + 1
    
print("We have " + str(greater_than_50) + " numbers greater than 50")
