# Python Focus Learning
# Functions Review
# Author: Kavan Lam
# Date: March 1, 2021

# Lets begin by looking at some pre-made functions that comes with Python/Processing
# Well you already seen a bunch of these
# Ex/ print, draw, setup, ellipse and so on

# Now lets talk about defining our own functions (easy example)
def double_me(something):
    print(something * 2)
    
double_me("Kavan")
double_me(50.5)


# Functions can return some value or they may not. This is very important to understand
print("-----------------------------------------------")
def double_me(something):
    return something * 2

result = double_me(21)
result = result + 1
print(result)


# Write a function which takes two numbers and returns the bigger of the two
print("---------------------------------------------")
def bigger_of_two(number1, number2):
    # num1 is the bigger one
    if number1 > number2:
        return number1
    # if num2 is the bigger one
    elif number1 < number2:
        return number2
    # is if they are the same
    else:
        return number1 # or return number2
        
result = bigger_of_two(100, 120)
print(result)


# Write a function which take 3 numbers and returns the bigger of the three
print("--------------------------------------------------")
def bigger_of_three(num1, num2, num3):
    my_list = [num1, num2, num3]
    return max(my_list)

result = bigger_of_three(2, -1, 5)
print(result)

# Write a function that takes a list of numbers prints out the list but with each number doubled




# Write a function that takes a list of numbers and for each number print whether it is odd or even (must use while loop)




# Write a function that takes a list of strings and for each strings it will print each character on a new line



# Functions can also have default values for parameters
