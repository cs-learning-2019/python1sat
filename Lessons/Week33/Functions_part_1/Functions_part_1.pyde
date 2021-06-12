# Focus Learning Python Level 1
# Functions part 1
# Kavan Lam
# June 5, 2021

# Ex 1
# Think of a function as a factory which will make something or do something.
# What the factory (function) produces or does is the output
# What the factory takes in is the input
# Every function start with a def also do not forget the brackets and :
def someStuff():
    print("Hello"*4)
    print("What's up!")
    
# To call the function simply use the name of the function
someStuff()
someStuff()

# print("dcsdchsbhdjcs")   print is also a function


# Ex 2
print("-----------------------------------------")
def multiply(num):
    print(num*7)
    
multiply(3)
multiply(5)
multiply(7)

print("-----------------------------------------")
def printLine(num_hash):
    print("#" * num_hash)
    
printLine(2)
printLine(4)
printLine(12)
printLine(12)
printLine(6)
printLine(2)

# Skill 3 Returning
print("-----------------------------------------")
def areaRect(side_length, side_width):
    return side_length * side_width
    
result = areaRect(2, 5)
print(result)
