# Python Level 1
# Intro to Python Week 2 HW solutions
# Kavan Lam
# Oct 11, 2021

# Question 1
age = 10
fav_number = 7

print("The total is " + str(age + fav_number))

# Question 2
"""
On line 3 we try to convert "13.5a" into an int but that is not possible since
"13.5a" is not a number since it has the "a". The second issue is on line 4
where we try to add a String with an integer which as discussed in class is
not possible in Python. You will have to convert age into a String first.
"""

# Question 3
print("*********")
print("*")
print("****")
print("*")
print("*")
print("*")
print("*")

# Question 4
print(3 ** 2 - (4 + 7) * 5)

# Question 5
score = 15
print("The score is " + str(score))

health = 77
print("The health is " + str((health * 6) % 4))

print("A" * score)
