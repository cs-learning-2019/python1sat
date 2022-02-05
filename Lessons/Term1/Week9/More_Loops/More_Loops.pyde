# Foucs Learning: Python Level 1 Cont
# More Loops with list
# Nov 20, 2020
# Kavan Lam

# Ex 1
for counter in range(0, 6):
    print(counter)
    

# Ex 2
print("--------------------------------")
counter = 0
while counter < 6:
    print(counter)
    counter = counter + 1
    
    
# Ex 3
print("----------------------------------")
myList = [15, 12, 3, 7]
for item in myList:
    print(item)
    

# Ex 4
print("----------------------------------")
myList = [15, 12, 3, 7]
index = 0
while index < len(myList):
    print(myList[index])
    index += 1  # This is shorthand notation for doing index = index + 1


# Ex 5
print("----------------------------------")
myList = [15, 12, 3, 7]
for counter in range(len(myList)):
    print(myList[counter])
    

# Ex 6
print("----------------------------------")
myList = [15, 12, 3, 7]
counter = 0
while counter < len(myList):
    print(myList[counter])
    counter += 1


# Ex 7
print("----------------------------------")
food = "peanut butter"
for letter in food:
    print(letter)

# Ex 8
print("----------------------------------")
food = "peanut butter"
counter = 0
while counter < len(food):
    print(food[counter])
    counter += 1

# Ex 9
print("----------------------------------")
greeting = "Hello earthlings!"
for index in range(len(greeting)-1, -1, -1):
    print(greeting[index])


# Ex 10
print("----------------------------------")
greeting = "Hello earthlings!"
counter = len(greeting) - 1 
while counter >= 0:
    print(greeting[counter])
    counter = counter - 1
    
# Ex 11
print("-----------------------------------")
toReverse = "Coding rocks!"
for index in range(len(toReverse)-1, -1, -1):
    print(toReverse[index])


# Ex 12
print("-----------------------------------")
toReverse = "Coding rocks!"
counter = len(toReverse) - 1
while counter >= 0:
    print(toReverse[counter])
    counter -= 1


"""
+= is just adding to a variable for example... a = a + 3 is the same thing as a += 3
also -= is just the same thing for exmaple a = a - 3 is the same thing as a -= 3
"""
