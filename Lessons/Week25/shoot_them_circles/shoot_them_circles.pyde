# Focus Learning: Python Level 1
# Shoot Them Circles
# Kavan Lam
# March 6, 2021

# HW
# NO Homework

# Steps
# 1) Setup the screen  [Done]
# 2) Create the character and allow it to move using WASD and ensure that the character can't leave the screen [Done]
# 3) Allow the character to shoot red lasers [Done]
# 4) Create the cirlce (bad guys) they will spawn randomly  [Almost Done]
# 5) Make the circles move towards the character


character_x = 400
character_y = 350
character_size = 100
character_speed = 10

circle_x = []
circle_y = []
circle_r = []
circle_g = []
circle_b = []

def setup():
    size(900, 900)

def draw():
    global character_x
    global character_y
    global character_size
    global circle_x
    global circle_y
    global circle_r
    global circle_g
    global circle_b
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the character
    rect(character_x, character_y, character_size, character_size)
    
    # Spawn a circle
    x = int(random(0, 900))
    y = int(random(0, 900))
    r = int(random(0, 255))
    g = int(random(0, 255))
    b = int(random(0, 255))
    
    circle_x.append(x)
    circle_y.append(y)
    circle_r.append(r)
    circle_g.append(g)
    circle_b.append(b)
    
    # Draw the circle
    for index in range(0, len(circle_x)):
        pushStyle()
        fill(circle_r[index], circle_g[index], circle_b[index])
        ellipse(circle_x[index], circle_y[index], 50, 50)
        popStyle()
    


def mousePressed():
    global character_x
    global character_y
    
    pushStyle()
    stroke(255, 0, 0)
    strokeWeight(5)
    line(character_x + (character_size / 2), character_y + (character_size / 2), mouseX, mouseY)
    popStyle()
    

def keyPressed():
    global character_x
    global character_y
    global character_size
    global character_speed
    
    if key == "W" or key == "w":  # Move up
       character_y = character_y - character_speed
       if character_y < 0:
           character_y = 0
    elif key == "D" or key == "d":  # Move right
       character_x = character_x + character_speed
       if character_x > 800:
           character_x = 800
    elif key == "S" or key == "s":  # Move down
       character_y = character_y + character_speed
       if character_y > 800:
           character_y = 800
    elif key == "A" or key == "a":  # Move left
       character_x = character_x - character_speed
       if character_x < 0:
           character_x = 0    
           
           
           
           
           
           
           
        
