# Python Focus Learning
# Functions Review
# Author: Kavan Lam
# Date: June 19, 2021

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

result = double_me(21)  # note 21 * 2 = 42
result = result + 1
print(result)


# Write a function which takes two numbers and returns the bigger of the two
print("---------------------------------------------")
def bigger_of_two(number1, number2):
    # number1 is the bigger one
    if number1 > number2:
        return number1
    # if number2 is the bigger one
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
print("--------------------------------------------------")
def double_my_numbers(num_list):
    for num in num_list:
        print(num * 2)


double_my_numbers([2, 6, 1, 0, 3])

# Write a function that takes a list of strings and for each strings it will print how many characters that string has
print("---------------------------------------------------")
def number_of_characters(str_list):
    for string in str_list:
        print(len(string))
    
number_of_characters(["hi", "bye", "hello", "PythonIsCool"])

# Write a function that takes a list of numbers and for each number print whether it is odd or even
print("---------------------------------------------------")
def is_even_or_odd(list_of_num):
    for num in list_of_num:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
    
is_even_or_odd([2, 3, 7, 10, 9, 1])
