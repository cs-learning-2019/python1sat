# Focus Learning: Python Level 1
# Shoot Them Circles
# Kavan Lam
# March 6, 2021

# Homework
# 1) Add more code to allow the character to be able to move down and to the left (make sure to prevent the character from leaving the screen)
# 2) The character can shoot red laser cool! However the outline of the chracter is also red and we do not want that so please fix it.

# Steps
# 1) Setup the screen  [Done]
# 2) Create the character and allow it to move using WASD and ensure that the character can't leave the screen
# 3) Allow the character to shoot red lasers [Done]
# 4) Create the cirlce (bad guys) they will spawn randomly

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
    
    stroke(255, 0, 0)
    line(character_x, character_y, mouseX, mouseY)
    

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
    # HOMEWORK: Allow the character to move to the Left and Down  (make sure to prevent the character from leaving the screen)
        
