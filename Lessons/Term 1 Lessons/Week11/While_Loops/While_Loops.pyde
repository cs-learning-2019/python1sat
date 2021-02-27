# Focus Learning: Python Level 1
# While loops
# Kavan Lam
# Nov 28, 2020


# Ex 1
print("---------------------------------")
# while (some condition):
counter = 8
while counter > 0:
    print(counter)
    counter = counter - 2
    

# Ex 2
print("---------------------------------")
counter = 1
while counter < 6:
    print("Hi!")
    counter = counter + 1


# Ex 3
print("---------------------------------")
counter = 2
while counter < 50:
    print(counter)
    counter = counter*counter


# Ex 4
print("---------------------------------")
counter = 2
while counter <= 6:
    print("-" * counter)
    counter = counter + 1


# Ex 5
print("---------------------------------")
passby = False  # This is a boolean
total = 0
while passby == False:
    total = total + 2
    if total > 12:
        print("!!!")
    if total > 20:
        passby = True
        

# Ex 6
print("---------------------------------")
# This is an exmaple of a infinite loop
"""
counter = 10
while counter > 0:
    print("This is amazing!")
    counter = counter + 1
"""
counter = 10
while counter > 0:
    print("This is amazing!")
    counter = counter - 1
