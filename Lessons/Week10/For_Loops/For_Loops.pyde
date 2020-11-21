# Focus Learning: Python Level 1
# For loops 
# Kavan Lam
# Nov 21, 2020

# We can print the numbers from 0 to 5 easily
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)

# Now what if we wanted to print the numbers from 0 to 100
# That is not easy and is takes too much time and work

# Is there a better method? Yes!!!!

# Ex 1
print("------------------------------------------")
# for (a variable) in (something):
for i in range(10): # Range will go one less than what you think
    print(i)
    
print("Hello")  # This line is not part of the for loop since there is no tab (4 spaces)

# Ex 2
print("------------------------------------------")
for j in range(8):
    print("&"*j)
    

# Ex 3
print("------------------------------------------")
for q in range(2, 7):
    print(str(q) + " cats")
   

# Ex 4
print("------------------------------------------")
for p in range(4, 10, 2):
    print(p*7)


# Ex 5
print("------------------------------------------")
for time in range(10, 0, -1):
    print(time)
print("Blastoff!")


# Ex 6
print("------------------------------------------")
for letter in "bugaboo":
    print(letter)

"""
# Ex 7
print("---------------------------------------")
size = 5
print("-" * size)
for row in range(size - 2):
    print("|" + " " * (size - 2) + "|")
print("-" * size)
"""
