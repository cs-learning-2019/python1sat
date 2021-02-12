# Focus Learning: Python Level 1 Cont
# Click and destroy objects
# Kavan Lam
# Dec 18, 2020

x = [12, 50, 300, 700]
y = [100, 200, 500, 700]
direction = [1, -1, 1, -1]

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    
    background(0, 0, 0)
    
    # Draw all the rectangles
    for index in range(len(x)):
        rect(x[index], y[index], 50, 50)
    
    # Move the rectangles
    for index in range(len(x)):
        x[index] = x[index] + (3 * direction[index])
    
    # Detect Bounce for all rectangles
    for index in range(len(x)):
        if x[index] <= 0:
            direction[index] = 1
        elif x[index] >= 850:
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
            pass
        else:
            x_new.append(x[index])
            y_new.append(y[index])
            direction_new.append(direction[index])
    
    x = x_new
    y = y_new
    direction = direction_new
    
    
