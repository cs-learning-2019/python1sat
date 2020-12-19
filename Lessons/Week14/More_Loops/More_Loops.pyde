# Foucs Learning: Python Level 1
# More Loops with list
# Dec 12, 2020
# Kavan Lam

# Ex 1
for counter in range(0, 6):
    print(counter)

print("range actually gives us a list")
print(range(0, 6))

# Ex 2
print("------------------------------")
counter = 0
while counter < 6:
    print(counter)
    counter = counter + 1
    

# Ex 3
print("------------------------------")
myList = [15, 12, 3, 7]
for item in myList:
    print(item)


# Ex 4
print("------------------------------")
myList = [15, 12, 3, 7]
index = 0
while index < len(myList):
    print(myList[index])
    index += 1  # The same as index = index + 1
    

# Ex 5
print("------------------------------")
myList = [15, 12, 3, 7]
for index in range(len(myList)):  # range(4) --> [0, 1, 2, 3]
    print(myList[index])
    
        
# Ex 6
print("-------------------------------")
myList = [15, 12, 3, 7]
index = 0
while index < len(myList):
    print(myList[index])
    index += 1  # The same as index = index + 1
    
# Ex 7
print("--------------------------------")
food = "peanut butter"
for letter in food:
    print(letter)
    
# Ex 8
print("--------------------------------")
food = "peanut butter"
index = 0
while index < len(food):
    print(food[index])
    index += 1
    
# Ex 9
print("--------------------------------")
greeting = "Hello earthlings!"  # Length is 17
for index in range(len(greeting)-1, -1, -1):
    print(greeting[index])


# Ex 10
print("--------------------------------")
greeting = "Hello earthlings!"
index = len(greeting) - 1
while index > -1:
    print(greeting[index])
    index = index - 1


# Ex 11
print("--------------------------------")
toReverse = "Coding rocks!"  # The length is 13
for index in range(len(toReverse)-1, -1, -1):
    print(toReverse[index])
 

# Ex 12
print("--------------------------------")
toReverse = "Coding rocks!"
index = len(toReverse)-1  # 12
while index > -1:
    print(toReverse[index])
    index -= 1  # Same as index = index - 1

 
 
 
 
 
