# Python Beginner
# Shoot Them Circles
# Feb 12, 2022

########## HOMEWORK #############
"""
1) Player should die when touched by a circle
"""

########## Next steps to work on during class (NOT HOMEWORK) #############
"""
2) player should die when touched by a circle
3) Add game over screen
4) Replace the square and circle with images of actual characters
5) Add music and sound effects into the game
6) Add ability to move diagonally 
"""

# Some variables for the character
character_x = 350
character_y = 350
character_speed = 5
character_alive = True  # or this could be False

# Some variables for the circles
circle_x = []
circle_y = []
spawn_timer = 0

# Other variables
score = 0

def setup():
    size(800, 800)
    
def draw():
    global character_x, character_y
    global circle_x, circle_y, spawn_timer
    global score
    
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
        character_center_x = character_x + 40
        character_center_y = character_y + 40
        distance = dist(random_x, random_y, character_center_x, character_center_y)
        if (distance > 120):
            circle_x.append(random_x)
            circle_y.append(random_y)
    
    # Draw the circles
    for colNum in range(len(circle_x)):
        pushStyle()
        fill(255, 0, 0)
        stroke(255, 141, 0)
        strokeWeight(3)
        ellipse(circle_x[colNum], circle_y[colNum], 50, 50)
        popStyle()
    
    # Move the circles closer to the character
    new_circle_x = []
    new_circle_y = []
    for colNum in range(len(circle_x)):
        # Take the position of the character and subtract it from the position of the circle
        difference_x = character_x + 40 - circle_x[colNum]
        difference_y = character_y + 40 - circle_y[colNum]
        
        if difference_x < 0:
            difference_x = -1
        elif difference_x > 0:
            difference_x = 1
        else:
            difference_x = 0
        
        if difference_y < 0:
            difference_y = -1
        elif difference_y > 0:
            difference_y = 1
        else:
            difference_y = 0
        
        # Find the new location of the circle
        new_x = circle_x[colNum] + difference_x
        new_y = circle_y[colNum] + difference_y
        
        # Add the new location to the list
        new_circle_x.append(new_x)
        new_circle_y.append(new_y)
        
    circle_x = new_circle_x
    circle_y = new_circle_y
        
    # Display the score
    textSize(50)
    fill(0, 0, 0)
    text("Score: " + str(score), 30, 50)
        
        
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
    global circle_x, circle_y
    global score
    
    # Draw the laser
    pushStyle()
    stroke(245, 62, 236)
    strokeWeight(4)
    line(mouseX, mouseY, character_x + 40, character_y + 40)
    popStyle()
    
    # Check if any of the circles died
    new_circle_x = []
    new_circle_y = []
    for colNum in range(len(circle_x)):
        distance = dist(mouseX, mouseY, circle_x[colNum], circle_y[colNum])
        if (distance > 50):
            new_circle_x.append(circle_x[colNum])
            new_circle_y.append(circle_y[colNum])
        else:
            score += 1
    
    circle_x = new_circle_x
    circle_y = new_circle_y
        
        
        
