# Focus Learning
# User interaction using the keyboard and mouse Homework Solutions
# Kavan Lam
# Aug 22, 2020

# Question 1
"""
You need to use keyCode when you want to detect something like arrow keys being pressed.
The difference is that key stores the string representing the button you pressed, but 
keyCode stores the code (which is a number) that represents the button pressed. Each 
button on the keyboard has a special number assigned to it.
"""

# Question 2   (When drawing the circle it should only flash and disappear)
def setup():
    size(900, 600)
    background(0, 0, 0)

x = 0
y = 0
def draw():
    global x
    global y
    
    # Clear previous frame
    background(0, 0, 0)
    
    # Update the rectangle location
    x = mouseX
    y = mouseY
    
    # Draw the rectangle
    rect(x - 25, y - 25, 50, 50)
    

def mousePressed():
    # Draw a circle
    pushStyle()
    fill(255, 0, 0)
    ellipse(mouseX, mouseY, 50, 50)
    popStyle()
    
    
    
    
