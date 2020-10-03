# Focus Learning
# Getting_Started_With_Processing_Homework SOLUTION
# Author: Kavan Lam
# Date: July 21, 2020


"""
Question 1
If we drew a dot/point at position (600,900) then it will appear on the bottom right corner.
If we drew a dot/point at position (100,150) then it will appear on the top left corner.


Question 2
The first number is the x position of the top left corner of the rectangle.
The second number is the y position of the top left corner of the rectangle.
The third number is the length of the rectangle.
The fourth number is the width of the rectangle.


Question 3
The first number is the x position of the center of the oval/circle.
The second number is the y position of the center of the oval/circle.
The third number is the horizontal radius/length of the oval/circle.
The fourth number is the vertical radius/length of the oval/circle.
"""

# Question 4
def setup():
    size(900, 350)
    background(0, 0, 0)
    
def draw():
    # Draw the text
    pushStyle()
    # Here we can use textSize() to make the text bigger
    fill(0, 255, 0)
    text("Hello world", 415, 20)
    popStyle()
    
    # Draw the blue cirlce
    pushStyle()
    fill(0, 0, 255)
    ellipse(450, 100, 120, 120)
    popStyle()
    
    # Draw the white cirlce
    pushStyle()
    fill(255, 255, 255)
    ellipse(450, 170, 120, 120)
    popStyle()
    
    # Draw the red cirlce
    pushStyle()
    fill(255, 0, 0)
    ellipse(450, 240, 120, 120)
    popStyle()
    
    # Draw the green line
    pushStyle()
    stroke(0, 255, 0)
    line(120, 90, 360, 280)
    popStyle()
    
    # Draw the red line
    pushStyle()
    stroke(255, 0, 0)
    line(780, 90, 560, 280)
    popStyle()
    
    # Draw the red rectangle
    pushStyle()
    fill(255, 0, 0)
    rect(50, 70, 50, 250)
    popStyle()
    
    # Draw the yellow rectangle
    pushStyle()
    fill(255, 255, 0)
    rect(800, 70, 50, 250)
    popStyle()
    

    
