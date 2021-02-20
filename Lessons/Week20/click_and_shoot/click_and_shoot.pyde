# Focus Learning: Python Level 1
# Click and destroy objects
# Kavan Lam
# Feb 20, 2021

x = [12, 50, 300, 700]
y = [100, 200, 500, 700]
direction = [1, -1, 1, -1]  # -1 = Left and 1 = Right

def setup():
    size(900, 900)
    
def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the rectangles
    for index in range(0, len(x)):
        rect(x[index], y[index], 50, 50)
    
    # Move the rectangles
    for index in range(0, len(x)):
        x[index] = x[index] + (5 * direction[index])
    
    # Bounce off the walls
    for index in range(0, len(x)):
        if x[index] <= 0:  # Left wall
            direction[index] = 1
        elif x[index] >= 850:  # Right wall
            direction[index] = -1
    
def mousePressed():
    global x
    global y
    global direction
    
    x_new = []
    y_new = []
    direction_new = []
    
    for index in range(len(x)):
        if mouseX >= x[index] and mouseX <= x[index] + 50 and mouseY >= y[index] and mouseY <= y[index] + 50:
            pass  # Special command to tell Python to do nothing
        else:
            x_new.append(x[index])
            y_new.append(y[index])
            direction_new.append(direction[index])
    
    x = x_new
    y = y_new
    direction = direction_new
