# Python Beginner
# Week 15 Homework Solutions
# Kavan Lam
# Jan 29, 2022

# Some variables for the first ball
x1 = 100
y1 = 100
direction1 = 1
visible1 = True

# Some variables for the second ball
x2 = 300
y2 = 150
direction2 = -1
visible2 = True

# Some variables for the background color
r = 0
g = 0
b = 0

def setup():
    size(700, 700)

def draw():
    global x1, y1, direction1, visible1
    global x2, y2, direction2, visible2
    global r, g, b
    
    # Clear the frame
    background(r, g, b)
    
    # Draw the balls
    fill(0, 0, 255)
    if visible1 == True:
        ellipse(x1, y1, 50, 50)
        
    if visible2 == True:    
        ellipse(x2, y2, 80, 80)
    
    # Make the balls move
    y1 = y1 + (direction1 * 5)
    y2 = y2 + (direction2 * 8)
    
    # Make the balls bounce
    # Deal with the first ball
    if y1 <= 50:
        direction1 = 1
    elif y1 >= 650:
        direction1 = -1
        
    # Deal with the second ball
    if y2 <= 80:
        direction2 = 1
    elif y2 >= 620:
        direction2 = -1
        
def keyPressed():
    global visible1
    global visible2
    
    if key == "A" or key == "a":
        # Make one of the circles disappear
        if visible1 == True and visible2 == True:
            visible1 = False
        elif visible1 == False and visible2 == True:
            visible2 = False

def mousePressed():
    global r, g, b
    
    r = int(random(0, 255))
    g = int(random(0, 255))
    b = int(random(0, 255))

    
    
    
    
    
    
    
    
