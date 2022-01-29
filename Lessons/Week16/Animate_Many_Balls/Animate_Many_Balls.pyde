# Python Beingnners
# Animate more than 2 balls  (6 balls in this exmaple)
# Kavan Lam
# Jan 29, 2022

x = [100, 200, 300, 400, 500, 600]
y = [200, 200, 100, 50, 150, 600]
direction = [1, -1, -1, 1, -1, 1]

def setup():
    size(700, 700)
    
def draw():
    global x, y, direction
    
    # Clear previous frame
    background(0, 0, 0)
    
    # Draw the balls
    for index in range(0, 6):
        fill(0, 255, 0)
        ellipse(x[index], y[index], 50, 50)
    
    # Move the balls
    for index in range(0, 6):
        y[index] = y[index] + (direction[index] * 5)
    
    # Make the balls bounce
    for index in range(0, 6):
        if y[index] <= 50:
            direction[index] = 1
        elif y[index] >= 650:
            direction[index] = -1
    
    
    
