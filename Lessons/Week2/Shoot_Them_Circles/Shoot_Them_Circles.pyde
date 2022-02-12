# Python Beginner
# Shoot Them Circles
# Feb 5, 2022

########## HOMEWORK #############
"""
1) The character is unable to move to the left or down. Please edit the code so this works.
2) The character is able to leave to screen through the left wall and bottom wall. Add code to block the player from
   moving off the screen
3) The crosshair is missing the left and bottom lines. You need to add code to include them.
"""

# Some variables for the character
character_x = 350
character_y = 350
character_speed = 5

def setup():
    size(800, 800)
    
def draw():
    global character_x, character_y
    
    # Clear the previous frame (draw the background)
    background(132, 188, 242)
    
    # Draw the character
    fill(132, 242, 182)
    rect(character_x, character_y, 80, 80)
    
    # Draw the crosshair
    pushStyle()
    stroke(255, 0, 0)
    strokeWeight(3)
    line(mouseX, mouseY - 8, mouseX, mouseY - 35)
    line(mouseX + 8, mouseY, mouseX + 35, mouseY)
    popStyle()

def keyPressed():
    global character_x, character_y, character_speed
    
    # Move up
    if key == "w" or key == "W":
        character_y = character_y - character_speed
        # We also need to check if the character went through the top wall
        if character_y < 0:
            character_y = 0
    # Move right
    elif key == "d" or key == "D":
        character_x = character_x + character_speed
        # We also need to check if the character went through the top wall
        if character_x > 720:
            character_x = 720

def mousePressed():
    print(mouseX, mouseY)
    
        
        
        
        
        
        
        
