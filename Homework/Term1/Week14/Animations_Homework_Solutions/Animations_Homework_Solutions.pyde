# Focus Learning
# Animations Homework Solutions
# Kavan Lam
# Jan 30, 2020

"""
# Questions 1
x_pos = 100
y_pos = 100
speed = 3
direction = 1

def setup():
    size(900, 900)
    
def draw():
    global x_pos
    global y_pos
    global speed
    global direction
    
    # Clear previous frame
    background(0, 0, 0)
    
    # Draw the ball
    ellipse(x_pos, y_pos, 50, 50)
    
    # Move the ball
    x_pos = x_pos + (speed * direction)
    
    # Detect the ball hitting the walls
    if x_pos >= 850:
        direction = -1
        speed = speed + 1
    elif x_pos <= 50:
        direction = 1
        speed = speed + 1 
"""

"""
# Questions 2
x_pos = 450
y_pos = 450

def setup():
    size(900, 900)
    
def draw():
    global x_pos
    global y_pos
    
    # Clear previous frame
    background(0, 0, 0)
    
    # Draw the square
    rect(x_pos, y_pos, 50, 50)
    
    # Move the square
    x_pos = x_pos + 5
    y_pos = y_pos - 5
"""

# Questions 3
x_pos = 100
y_pos = 100
direction = 1
play = True
ball_color = 0

def setup():
    size(900, 600)
    
def draw():
    global x_pos
    global y_pos
    global play
    global direction
    global ball_color
    
    # Clear previous frame
    background(0, 0, 255)
    
    # Draw the ball
    fill(ball_color, ball_color, ball_color)
    ellipse(x_pos, y_pos, 50, 50)
    
    # Move the ball
    if play == True:
        y_pos = y_pos + (10 * direction)
    
    # Detect the ball hitting the walls
    if y_pos >= 550:
        direction = -1
    elif y_pos <= 50:
        direction = 1

def keyPressed():
    global play
    global ball_color
    
    if key == "S" or key == "s":
        play = False
    elif key == "P" or key == "p":
        play = True
    elif key == "C" or key == "c":
        ball_color = ball_color + 20
