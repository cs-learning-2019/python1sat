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
# 4) Create the cirlce (bad guys) they will spawn randomly  [Almost there (We talked about how to do this)]
# 5) Make the circles move towards the character

character_x = 400
character_y = 350
character_size = 100
character_speed = 10

def setup():
    size(900, 900)

def draw():
    global character_x
    global character_y
    global character_size
    
    # Clear the previous frame
    background(0, 0, 0)
    
    rect(character_x, character_y, character_size, character_size)


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
           
           
           
           
           
           
           
        
