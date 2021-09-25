# Intro to Python
# Sept 25, 2021
# Kavan Lam

# Skill 1: Printing - Part A
print("Welcome to Python!")
print("What are \nthese hacks?") # \n makes you go to the next line
print("\t What is going on? :)")  # \t is the same thing as tab (5 space)
print("SPAM " * 5)  # * means multiplication

# Challenges
# A)
print("Baseball")

# B)
print("*" * 9)
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("*" * 9)

# Pratice Questions
# 1) \n is a special word that makes Python skip to the next line
# 2) It just prints the string by the amount you mulitplied by

# Skill 2: Printing - Part B (Concatenation)
print("---------------------------------------------------------")
# concatenation is a fancy word for adding
print("Hello" + " What is this?")  # This is called string concatenation
print("Banana " * 3 + "Orange you glad I didn't say banana?")
print("\t"*2 + "-.-.- " * 5 + "|||")

# Challenges
# A)
print("Kavan" + " " + "Lam")
# B) Skip this one

# Practice Questions
# 1) We use the + symbol
# 2) Usually in programming we will have different pieces of data in different places
#    and concatenation will allow use to combine the pieces of data into one.
# 3) 
print("You're amazing!" + " And the best!" + " And better than all the rest!")
# 4) There is a space since there is a space before the A


# Skill 3: Variables
print("-----------------------------------------------------------------------------")
# A variable is like a helping hand that can hold on to data for you.
# You have to give the variable a name
# When naming your variables you need to follow these rules
# 1) No spaces allowed, but you can use _ (underscore) instead
# 2) No special characters except _. So in other words only numbers and letter.
# 3) Your variable name must begin with a letter
# Note, uppercase and lowercase is both fine
bugs = 10
colour = "Red"
like_cheese = False
fav_num = 54.3

# There are different kinds of data that variables can hold on to
# 1) int ex/ 2, 3, -5, 10, 99, 6789, -1
# 2) String ex/ "john", "john _ = 234567", "[]#TGREcdbfui43fu8i32fk", "True"
# 3) boolean ex/ True, False
# 4) float (A number with decimal) ex/ 54.3, 99.0, 1.1, -5.67

print(colour)
print(fav_num)
#print(my_variable) not going to work since we never created this variable

# You can not add a string with an int/float
x = "Kavan"
y = 10
print("My name is " + x + " and my age is " + str(y))
