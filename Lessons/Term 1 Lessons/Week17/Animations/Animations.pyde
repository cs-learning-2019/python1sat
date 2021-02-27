# Focus Learning: Python Level 1
# Animations
# Kavan Lam
# Jan 23, 2020


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
    rect(x, y, 50, 50)
    
    # Changing the position the circle
    y = y + (direction * 5)   # If direction = 1 then y = y+5 . If direction = -1 then y = y - 5
    
    # Detect collision with the top and bottom wall
    if y >= 900:  # If you hit the bottom wall
        direction = -1
    elif y <= 0:  # If you hit the top wall
        direction = 1
"""  

# Section 4
"""
x = 450  # Left and right 
y = 450  # Up and down
direction = 1  # 1 = move down    -1 = move up
direction_of_animation = "Vertical"  # Or it is "Horizontal"

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    global direction_of_animation
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle
    ellipse(x, y, 50, 50)
    
    # Changing the position the circle
    if direction_of_animation == "Vertical":
        y = y + (direction * 5)   # If direction = 1 then y = y+5 . If direction = -1 then y = y - 5
    elif direction_of_animation == "Horizontal":
        x = x + (direction * 5)
        
    # Detect collision with the top and bottom wall
    if y >= 900:  # If you hit the bottom wall
        direction = -1
    elif y <= 0:  # If you hit the top wall
        direction = 1
    
    if x >= 900:  # If you hit the right wall
        direction = -1
    elif x <= 0:  # If you hit the left wall
        direction = 1
        
def mousePressed():
    global direction_of_animation
    # Change the direction of animation
    print("The mouse was pressed")
    if direction_of_animation == "Vertical":
        direction_of_animation = "Horizontal"
    elif direction_of_animation == "Horizontal":
        direction_of_animation = "Vertical"
"""

# Section 5
x = 450
y = 450
direction = 1  # 1 = move down    -1 = move up
num_bounces = 0  # This variable will keep track of the number of bounces

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    global num_bounces
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle
    ellipse(x, y, 50, 50)
    
    # Draw some text
    pushStyle()
    textSize(40)
    fill(0, 255, 255)
    text("Number of bonuces: " + str(num_bounces), 100, 100)
    popStyle()
    
    # Changing the position the circle
    y = y + (direction * 5)   # If direction = 1 then y = y+5 . If direction = -1 then y = y - 5
    
    # Detect collision with the top and bottom wall
    if y >= 900:  # If you hit the bottom wall
        direction = -1
        num_bounces = num_bounces + 1
    elif y <= 0:  # If you hit the top wall
        direction = 1
        num_bounces = num_bounces + 1
