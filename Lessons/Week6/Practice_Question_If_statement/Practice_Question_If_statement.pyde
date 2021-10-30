# Python Level 1
# Week 6 Lesson
# Kavan Lam
# Oct 30, 2021

"""
Answer the following question: Given a string and an integer print "Hello there" if the string contains the substring "yo",

prints "boo" if the string contains the substring "ah" and the integer is greater than 15.

Also print "Oh no" if the integer is even or the string contains and odd amount of characters.
"""

word = "Bunny"
age = 18

if "yo" in word:
    print("Hello there")
elif ("ah" in word) and (age > 15):
    print("boo")
elif (age % 2 == 0) or (len(word) % 2 != 0):  # Note that len is short for length   also ! means not
    print("oh no")
    

print("-------------------------------------------------------------")
# Lets talk about len (the length command)
name = "Sunny"
print(len(name))
