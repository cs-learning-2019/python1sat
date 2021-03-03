# Focus Learning Python Level 1
# Pre-Project work
# Kavan Lam
# Feb 27, 2021

x = [300, 600]
y = [450, 450]
direction = [1, -1]  # 1 --> move down , -1 --> move up
color_r = 0
color_g = 0
color_b = 0

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    global color_r
    global color_g
    global color_b
    
    # Clear previous frame
    background(color_r, color_g, color_b)
    
    # Draw the balls
    for index in range(0, len(x)):
        ellipse(x[index], y[index], 50, 50)
        
    # Move the balls
    for index in range(0, len(x)):
        y[index] = y[index] + (5 * direction[index])
        
    # Bounce of the walls
    for index in range(0, len(x)):
        if y[index] <= 50:
            direction[index] = 1
        elif y[index] >= 850:
            direction[index] = -1
            
def keyPressed():
    global x
    global y
    global direction
    
    # Detect if the user actually clicked on A or a
    if key == "A" or key == "a":
        # Remove a ball
        x.pop()
        y.pop()
        direction.pop()
    
def mousePressed():
    global color_r
    global color_g
    global color_b
    
    color_r = int(random(0, 255))
    color_g = int(random(0, 255))
    color_b = int(random(0, 255))
    
    
    
    
    
            
