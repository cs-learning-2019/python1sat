# Basic math operators in Python
print(4 + 1)
print(4 - 1)
print(3 * 2)
print(3 / 2)  # This should give us 1.5 but it actually gives up 1

# In Python when you divide numbers the result will either be an int
# or a float.
# Here is the rule, if the numerator or denominator is a float then the
# result will also be a float. Otherwise the answer will be a int.
print("-------------------------------------------------------------")
print(7 / 2)
print(7.0 / 2)

# You can do exponents in Python
print("-------------------------------------------------------------")
print(3 ** 2)  # 3 raised to the exponent 2 is 9
print(2 ** 4)  # 2 rasied to the exponent 4 is 16

# You can do sqrt in Python
print("-------------------------------------------------------------")
print(sqrt(4))  # What number times itself is 4? It is 2
print(sqrt(9))  # What number times itself is 9? It is 3

# You can do div (integer division) in Python
print("-------------------------------------------------------------")
print(7.0 / 3) # This is just normal divison so you get 2.3333
print(7.0 // 3) # This gives you 2 and NOT 2.3333 since // removes the decimal

# To get the remainder of a divison you can use mod
print("-------------------------------------------------------------")
print(7.0 % 3)  # What is the remainder after dividing 7 by 3? It is 1
print(82 % 2)   # 82 divide by 2 has no remainder since 82 is even

# Data type conversion - convert a number into a string
print("-------------------------------------------------------------")
number = -27.525
new_number = str(number)  # "-27.525"
print(type(number))
print(type(new_number))  # The type command gives you the data type

# Data type conversion - convert a string into a number (You need to be carful about this one)
print("-------------------------------------------------------------")
number = "34.5"
new_number = float(number)
print(type(number))
print(type(new_number))
print(new_number + 1)

bad_number = "24a.1"
# bad_new_number = float(bad_number)

# Q1) Write Python Code to ask the user for their height and print out "Your height will be <height + 10> soon"
print("-------------------------------------------------------------")
my_height = 150
print("Your height will be " + str(my_height + 10) + " soon")

# Q2) Write Python Code to print out the letter H
print("-------------------------------------------------------------")
print("*    *")
print("*    *")
print("******")
print("*    *")
print("*    *")

# Q3) Write Python Code to print out the answer to the following (10-4)/5x4^2
print("-------------------------------------------------------------")
print((10 - 4) / 5 * 4 ** 2)
