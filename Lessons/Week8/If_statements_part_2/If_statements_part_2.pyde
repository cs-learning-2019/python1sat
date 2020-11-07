# Focus Learning: Python 1 Level
# If statement part 2
# Kavan Lam
# Nov 7, 2020

# Skill 1 (And Operator)
wantCheese = True
wantBacon = True
if wantCheese == True and wantBacon == True:
    print("Bacon Cheese Burger")
elif wantCheese == True and wantBacon == False:
    print("Cheese Burger")

# and <---- This is one of the logical operators that you can use
# If you use "and" everything needs to be true for it to continue

# Challenge A (Truth Table)
"""
A    B    A and B
T    T    T
T    F    F
F    T    F
F    F    F
"""


# Skill 2 (Or Operator)
print("--------------------------------------------------")
wantCream = False
wantSugar = False
if wantCream == True or wantSugar == True:
    print("Offer cream, offer sugar")
else:
    print("Don't offer either")

# Challenge B (Truth Table)
"""
A    B    A OR B
T    T    T
T    F    T
F    T    T
F    F    F
"""


# Skill 3 (Not Operator)
print("--------------------------------------------------")
fiction = True
if not(fiction == True):
    print("This is a true story")
else:
    print("This is a made up story")
"""
A    NOT A
T    F
T    F
F    T
F    T
"""






    
    
    
    
    
    
    
    
