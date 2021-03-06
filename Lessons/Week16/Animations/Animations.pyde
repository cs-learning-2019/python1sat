# Focus Learning: Python Level 1
# Animations
# Kavan Lam
# Jan 16, 2020


# Contents
# 1) Simple animation of a ball moving to the right
# 2) Animation of a ball moving up and down (bouncing off walls)
# 3) Same as 2 but with a square
# 4) Be able to switch the direction of animation with mouse pressed
# 5) Keep track of number of bounces and display on the screen



# Section 1
"""
x = 100
y = 450

def setup():
    size(900, 900)

def draw():
    global x
    global y
    
    # Clear the previous frame
    background(0, 0, )
    
    # Draw the circle
    ellipse(x, y, 50, 50)
    
    # Changing the position the circle
    x = x + 5
"""

# Section 2
"""
x = 450
y = 450
direction = 1  # 1 = move down    -1 = move up

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle
    ellipse(x, y, 50, 50)
    
    # Changing the position the circle
    y = y + (direction * 5)   # If direction = 1 then y = y+5 . If direction = -1 then y = y - 5
    
    # Detect collision with the top and bottom wall
    if y >= 900:  # If you hit the bottom wall
        direction = -1
    elif y <= 0:  # If you hit the top wall
        direction = 1
"""    

# Section 3
x = 450
y = 450
direction = 1  # 1 = move down    -1 = move up

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle
    rect(x, y, 50, 50)
    
    # Changing the position the circle
    y = y + (direction * 5)   # If direction = 1 then y = y+5 . If direction = -1 then y = y - 5
    
    # Detect collision with the top and bottom wall
    if y >= 900:  # If you hit the bottom wall
        direction = -1
    elif y <= 0:  # If you hit the top wall
        direction = 1
  





























# Solutions
"""
# Section 1
x = 100
y = 300
def setup():
    size(900, 900)


def draw():
    global x
    global y
    background(0, 0, 0)
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # move the circle
    x = x + 10
"""    

"""
# Section 2
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction 
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # move the circle
    y = y + (direction * 10)
    
    # Check for collision
    if y <= 0:

                direction = 1
    elif y >= 900:
        direction = -1
"""

"""
# Section 3
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction 
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    rect(x, y, 50, 50)
    
    # move the circle
    y = y + (direction * 5)
    
    # Check for collision
    if y <= 0:
        direction = 1
    elif y >= 850:
        direction = -1
"""

"""
# Section 4
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up
case = 1 # Either 1 or 2 --> 1 = Move up and down and 2 = move left and right

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction 
    global case
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # move the circle
    if case == 1:
        y = y + (direction * 10)
    elif case == 2:
        x = x + (direction * 10)
    
    # Check for collision
    if x <= 0:
        direction = 1
    elif x >= 900:
        direction = -1
        
    if y <= 0:
        direction = 1
    elif y >= 900:
        direction = -1

def mousePressed():
    global case
    
    if case == 1:
        case = 2
    elif case == 2:
        case = 1
"""
"""
# Section 5
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up
case = 1 # Either 1 or 2 --> 1 = Move up and down and 2 = move left and right
num_bounce = 0

def setup():
    global font1
    
    size(900, 900)
    font1 = loadFont("BerlinSansFB-Bold-48.vlw")

def draw():
    global x
    global y
    global direction 
    global case
    global num_bounce
    global font1
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # Draw some text
    pushStyle()
    textFont(font1, 30)
    text("The number of bounces: " + str(num_bounce), 50, 50)
    popStyle()
    
    # move the circle
    if case == 1:
        y = y + (direction * 10)
    elif case == 2:
        x = x + (direction * 10)
    
    # Check for collision
    if x <= 0:
        direction = 1
        num_bounce = num_bounce + 1
    elif x >= 900:
        direction = -1
        num_bounce = num_bounce + 1
        
    if y <= 0:
        direction = 1
        num_bounce = num_bounce + 1
    elif y >= 900:
        direction = -1
        num_bounce = num_bounce + 1

def mousePressed():
    global case
    
    if case == 1:
        case = 2
    elif case == 2:
        case = 1
"""
