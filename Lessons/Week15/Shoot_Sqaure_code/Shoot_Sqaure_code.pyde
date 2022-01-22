# Python Beginner
# Shoot moving sqaure
# Kavan Lam
# Jan 22, 2022

x = 300
y = 300
alive = True

def setup():
    size(700, 700)
    
def draw():
    global x
    global y
    
    # Clear the previous frame
    if alive == True:
        background(0, 255, 0)
    else:
        background(0, 0, 0)
    
    if alive == True:
        # Draw the rectangle
        fill(255, 100, 0)
        rect(x, y, 50, 50)
        
        # Move the rectangle
        x = x + int(random(-20, 20))
        y = y + int(random(-20, 20))

def mousePressed():
    global x
    global y
    global alive
    
    # We need to detect if the mouse is inside the square
    if mouseX >= x and mouseX <= x + 50 and mouseY >= y and mouseY <= y + 50:
        alive = False
