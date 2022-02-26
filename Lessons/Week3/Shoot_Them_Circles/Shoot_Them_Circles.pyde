# Python Beginner
# Shoot Them Circles
# Feb 12, 2022

########## HOMEWORK #############
"""
1) Make the circle red with a orange border
2) Make sure the circles do not spawn too close to the character
3) Challenge: When you click on a circle the circle should die and disappear
"""

########## Next steps to work on during class (NOT HOMEWORK) #############
"""
1) Make the circles move towards the player
2) Add score into the game
3) Add game over screen
4) Replace the square and circle with images of actual characters
5) Add music and sound effects into the game
6) Add ability to move diagonally 
"""

# Some variables for the character
character_x = 350
character_y = 350
character_speed = 5

# Some variables for the circles
circle_x = []
circle_y = []
spawn_timer = 0

def setup():
    size(800, 800)
    
def draw():
    global character_x, character_y
    global circle_x, circle_y, spawn_timer
    
    # Clear the previous frame (draw the background)
    background(132, 188, 242)
    
    # Draw the character
    fill(132, 242, 182)
    rect(character_x, character_y, 80, 80)
    
    # Draw the crosshair
    pushStyle()
    stroke(255, 255, 0)
    strokeWeight(3)
    # Top line
    line(mouseX, mouseY - 8, mouseX, mouseY - 35)
    # Right line
    line(mouseX + 8, mouseY, mouseX + 35, mouseY)
    # Bottom line
    line(mouseX, mouseY + 8, mouseX, mouseY + 35)
    # left line
    line(mouseX - 8, mouseY, mouseX - 35, mouseY)
    popStyle()
    
    # Spawn new circle
    spawn_timer = spawn_timer + 1
    if spawn_timer == 45:
        spawn_timer = 0
        random_x = int(random(0, 800))
        random_y = int(random(0, 800))
        circle_x.append(random_x)
        circle_y.append(random_y)
    
    # Draw the circles
    for colNum in range(len(circle_x)):
        ellipse(circle_x[colNum], circle_y[colNum], 50, 50)
        
        
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
        # We also need to check if the character went through the right wall
        if character_x > 720:
            character_x = 720
    # Move left
    elif key == "a" or key == "A":
        character_x = character_x - character_speed
        # We also need to check if the character went through the left wall
        if character_x < 0:
            character_x = 0
    # Move down
    elif key == "s" or key == "S":
        character_y = character_y + character_speed
        # We also need to check if the character went through the top wall
        if character_y > 720:
            character_y = 720

def mousePressed():
    global character_x, character_y
    pushStyle()
    stroke(245, 62, 236)
    strokeWeight(4)
    line(mouseX, mouseY, character_x + 40, character_y + 40)
    popStyle()
    
        
        
        
        
        
        
        
