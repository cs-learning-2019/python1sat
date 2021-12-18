# Python Beginner
# Week 12 HW
# Kavan Lam
# Dec 17, 2021

# Question 1
"""
mouseX and mouseY are variables automatically created and managed
by Python/Processing. The two variables together allow you to keep
track of the position of the mouse on the screen
"""

# Question 2
"""
First you need to create x and y variables to keep track of the position
of the shape. Then when drawing the shape you need to use the x and y
variables instead of using a number. Finally you need a keyPressed section.
The computer knows that you pressed the arrow keys by using keyCode.
"""

# Question 3
"""
should_flash = True
r = 255
g = 0
b = 0

def setup():
    size(500, 500)
    
def draw():
    global should_flash
    global r
    global g
    global b
    
    background(0, 0, 0)
    
    if should_flash == True:
        r = int(random(0, 255))
        g = int(random(0, 255))
        b = int(random(0, 255))
    
    fill(r, b, g)
    ellipse(250, 250, 50, 50)
    
def keyPressed():
    global should_flash
    
    # Up arrow key
    if keyCode == 38:
        should_flash = True
    # Down arrow key
    elif keyCode == 40:
        should_flash = False
"""

# Question 4
def setup():
    size(500, 500)
    
def draw():
    background(0, 0, 0)
    rect(mouseX - 25, mouseY - 25, 50, 50)
