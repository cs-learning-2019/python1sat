# Focus Learning Python Level 1
# Intro to Python
# Sept 20, 2020
# Kavan Lam


### Skill 1 ###
# This is a comment I can say wahtever I want
print("Welcome to Python!")
print("What are \n these hacks?") # \n = newline (is a special character that moves to the next line)
print("\t What is going on? :)")  # \t = tab = 4 spaces
print("SPAM" * 20)  # the * means multiplication

# print is a command but really we should call it a function

# Challenges
# A
print("Baseball")
# B
print("*" * 9)
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("*" * 9)

### Skill 2 ###
print("-----------------------------------------------------------------------")
# Concatenation is a fancy word for addition
# A string is anything inside " "  <---- quotes. A string is kind of like a sentence
print("Hello" + " What is this?")
print("Banana " * 3 + "Orange you glad I didn't say banana?")
print("\t"*2 + "-.-.- " * 5 + "|||")

# Challenges
# A
print("Kavan " + "Lam")
# B
print("*" * 9)
print("*       *")
print("*" + " Kavan " + "*")
print("*       *")
print("*       *")
print("*" * 9)

# Practice Question
# 2
""" This is a multi-line comment
The reason why concatenation is useful is bacause you may have many different strings
that you may want to combine into a single string. Also you can create cool output with it.
"""
# 3 
print("You're amazing!" + " And the best!" + "And better than all the rest!")


### Skill 3 ###
print("---------------------------------------")
# Rules for naming variables
# 1) No spaces
# 2) No Special character (Only use numbers and letters)
# 3) Can not start with a number
bugs = 11  # bugs is a variable  we call this an integer = int
colour = "Blue" # We call this a string
like_cheese = True  # We call this a boolean 
fav_num = 12.323  # We call this a float (any number with a decimal point is called a float)

print(bugs)
print("My favourite colour is " + colour)
print(like_cheese)
print(fav_num*10)

# Challenges
shoe_sz = 8
print("My shoe size is " + str(shoe_sz))
