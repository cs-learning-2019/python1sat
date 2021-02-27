# Focus Learning: Python Level 1 Cont
# For Loops Homework Solution
# Kavan Lam
# Oct 24, 2020

# Question 1
"""
A for loop is one of the main types of loops you can use in Python. It allows
you to do something over and over again and in particular you can loop over 
objects like a collection of numbers or a string.
"""

# Question 2
"""
There are two issues.
1) The range function is used incorrectly. You (0, 10, -1) which means start at 0 and stop at 9
   but count by -1 which means go in reverse. You can not go from 0 to 10 by counting backwards.
2) Inside the print we have print(x) but the loop variable is num so we need to say print(num)
"""

# Question 3
word = "Home"
for character in word:
    print(character * 6)
