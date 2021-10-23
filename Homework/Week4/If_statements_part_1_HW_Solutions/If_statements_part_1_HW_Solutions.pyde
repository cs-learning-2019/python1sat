# Python Level 1
# If statements part 1 HW Solutions
# Kavan Lam
# Oct 23, 2021

# Question 1
"""
If statements allow the computer to make decisions and do different things
based on different cases. If statements always begin with the keyword "if"
and can be extended by using "elif" and "else".
"""

# Question 2
age = 12
if age > 65:
    print("You are old")
elif age >= 18:
    print("You are an adult")
elif age < 18:
    print("You are young")

# Question 3
sides = 3
special_message = "I am a special shape"

if sides == 3:
    print("You are a triangle")
elif sides == 4:
    print("You are a rectangle")
elif sides > 4:
    print("You are a polygon")
    
if sides == 3:
    print(special_message)
    
# Question 4
"""
The second and third case use the "if" keyword but it should use "elif" so
that the whole thing is treated as one if statement. The second case has :70
which is the wrong order. It should be 70: since the colon should come after
"""

# Question 5
favourite_word = "Amazing"

if "A" in favourite_word:
    print("My favourite word has an A in it")
    if "M" in favourite_word:
        print("My favourite word also has a M in it")
    
    
    
    
