# Focus Learning
# If statements part 2 Homework Solutions
# Kavan Lam
# Aug 11, 2020

# Question 1
"""
The AND operator will only result in True when everything is true, but the OR operator will
result in true as long as there is at least one thing that is true. Basically the AND operator
is very scrict, but the OR operator is not. A single equal sign is used for assigning a value to
a variable (assignment statement), but a double equal sign is used as a comparision. The double
equal sign lets you compare two things to see if they are the same.
"""

# Question 2
x = 10 
y = 5 
 
if x > 15 or (x + y > 16):  
    print("Nice job") 
elif x - y <= 5:  
    print("Cool") 
else:
    print("Nothing")


# Question 3
x = 100 
y = 100 
direction = "Right" 
 
if direction == "Right":  
    x = x + 10
elif direction == "Down":
    y = y + 20
elif direction == "Left":
    x = x - 10
elif direction == "Up":
    y = y - 20
 
