# Focus Learning: Python Level 1
# If statements part 1
# Kavan Lam
# Oct 31, 2020

# Skill 1
# if (condition):   <--- General form  note : means then
# <  means less than
# >  means more than
# Ex1
if 3 < 5:
    print("Pikachu!")
    
print("Hello")  # This is not part of the if statement because it does not have a tab
    
# Ex2
print("------------------------------------------")
amt = 21
if amt == 20:
    print("$20")
else:  # This is like the last resort for the if statements
    print("Money")

# Note: A single equation sign is for taking something and storing it into a variable
# A double equal sign is for comparing. Is amt holding onto the number 20?

# Challenges
# A)
print("------------------------------------------")
age = 40
if age > 12:
    print("You get a joke")
else:
    print("You not old enough")

# B)
print("------------------------------------------")
number = 600
if number % 2 == 0:  # The % gives you the remainder of a division
    print("Even")
else:
    print("Odd")
    

# Skill 2
# Ex 1
print("------------------------------------------")
mark = 95
if mark > 90:
    print("A+")
elif mark > 80:
    print("A")
elif mark > 70:
    print("B")
elif mark > 60:
    print("C")
elif mark > 50:
    print("D")
else:  # If you decide to use "else" it must be the last thing in your if statement
    print("Needs help.")
    
# BTW above is one single if statement. We begin a if statment with "if" and we can extend it
# using elif and else
# Also because the above is one single if statement then the first case that works is the only
# case that will get run.


# Practice Question 1
print("------------------------------------------")
a = 20

# First block of code
if a > 17:
    print("You're an adult")
    
if a > 13:
    print("You're a teenager")
else:
    print("You're a kid.") 

print("------------------------------------------")
# Second block of code
if a > 17:
    print("You're an adult")
elif a > 13:
    print("You're a teenager")
else:
    print("You're a kid.") 
    
# Practice Question 2
print("------------------------------------------")
peanut_sales = 200
if peanut_sales <= 200:
    print("You have not sold enough peanuts.")
else:
    print("Quota reached.")
    

# Practice Question 3
print("------------------------------------------")
month = 12
if month < 3:
    print("Winter")
elif month < 6:  # is 6 < 6 ???? NO it is NOT
    print("Spring")
elif month < 9:
    print("Summer")
else:
    print("Fall")
