# Focus Learning: Python Level 1 Cont
# List Homework Solutions
# Nov 4, 2020
# Kavan Lam

# Question 1
# a)
# [50, 500, 5, 50, 30, 10, -1]

# b)
# [6, 4, 5, 7, 8]

# c)
# [Bob, Lily, Stacy]

# Question 2
# We are doing x[4] but there is no such thing as index 4 in [1, 2, 5, 8]

# Question 3
names = ["John", "Bob", "Lu"]
index = 0
while index < len(names):
    print("Hello, how are you, " + names[index] + "?")
    index = index + 1
