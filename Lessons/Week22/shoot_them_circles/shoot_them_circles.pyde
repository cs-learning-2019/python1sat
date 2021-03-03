# Focus Learning: Python Level 1 Cont
# Shoot Them Circles
# Kavan Lam
# Jan 8, 2021

# Homework
# 1) Program the character to move using the S and D keys. Ensure that the character can't leave the screen.
# 2) Review lesson 14

# Steps
# 1) Setup the screen
# 2) Create the character and allow it to move using WASD and ensure that the character can't leave the screen
# 3) Allow the character to shoot yellow lasers (Later we will make the lasers stay on the screen for a bit)
# 4) Create the cirlce (bad guys) they will spawn randomly

character_x = 400
character_y = 400
character_speed = 10
character_size = 100

def setup():
    size(900, 900)

def draw():
    global character_x
    global character_y
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the character
    rect(character_x, character_y, character_size, character_size)
    
    # Draw the circles (bad guys)
    # Use a loop to go over all circles
    # ellipse(whatever the x is, whatever the y is, 30, 30)
    
def keyPressed():
    global character_x
    global character_y
    global character_speed
    
    if key == "W" or key == "w":
        character_y = character_y - character_speed
        if character_y < 0:
            character_y = 0
    elif key == "A" or key == "a":
        character_x = character_x - character_speed
        if character_x < 0:
            character_x = 0

def mousePressed():
    global character_size
    global character_x
    global character_y
    
    pushStyle()
    stroke(255, 255, 0)
    line(character_x + character_size/2, character_y + character_size/2, mouseX, mouseY)
    popStyle()
    
    
