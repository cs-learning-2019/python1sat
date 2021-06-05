# Focus Learning Python Level 1 cont
# Functions
# Kavan Lam
# Feb 22, 2021

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
# Notice that the function moreStuff calls the function stuff
def stuff():
    print("Potato " * 3)
    print("Pizza!")

def moreStuff():
    for i in range(3):
        stuff()

moreStuff()

# Ex 3
print("-----------------------------------------")
def printLine(num_hash):
    print("#" * num_hash)

printLine(2)
printLine(4)
printLine(11)
printLine(11)
printLine(6)
printLine(2)

# Ex 4
print("-----------------------------------------")
def superMultiply(a, b, c, d):
    print(a * b * c + d)

superMultiply(1, 2, 3, 1)


# Ex 5
print("-----------------------------------------")
def areaRect(L, W):
    print("The area is " + str(L * W))

areaRect(5, 6)


# Ex 6
print("-----------------------------------------")
def funkyWord(word):
    aWord = word.upper()  # BOY
    bWord = word.lower()  # boy
    cWord = aWord + bWord # BOYboy
    print(cWord)

funkyWord("HUmpy Dumpy")


# Functions part 1 HW solutions (last page)
print("------------------------------------")
def box_maker(num):
    print("*" * num)
    for row in range(num - 2):
        print("*" + " " * (num - 2) + "*")
    print("*" * num)

box_maker(9)
