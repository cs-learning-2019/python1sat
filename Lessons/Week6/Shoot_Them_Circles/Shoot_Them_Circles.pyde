# Python Beginner
# Shoot Them Circles
# Feb 12, 2022

########## HOMEWORK #############
"""
1) Finish game over screen (Add text to display the score and a message --> Either "You are a pro" or "You need practice")
2) Make the game over screen use better colors
"""

########## Next steps to work on during class (NOT HOMEWORK) #############
"""
4) Replace the square and circle with images of actual characters
5) Add music and sound effects into the game
6) Add ability to move diagonally
7) We should make the game harder as your score increases
8) Change the font style
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
    if (character_alive == True):
        playGame()
    else:
        gameOver()

def gameOver():
    # Clear the game screen
    background(120, 120, 120)
    
    # Draw the game over text
    pushStyle()
    textAlign(CENTER)
    textSize(60)
    fill(255, 0, 0)
    text("Game Over", 400, 130)
    popStyle()
    
    # Draw the play again button
    pushStyle()
    fill(255, 255, 255)
    rect(300, 400, 200, 50)
    textAlign(CENTER)
    textSize(30)
    fill(0, 0, 200)
    text("Play Again", 400, 435)
    popStyle()
    
def playGame():
    global character_x, character_y, character_alive
    global circle_x, circle_y, spawn_timer
    global score
    
    # Clear the previous frame (draw the background)
    background(132, 188, 242)
    
    # Draw the character
    if (character_alive == True):
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
    
    # Check to see if the character got touched by a circle
    for colNum in range(len(circle_x)):
        distance = dist(character_x + 40, character_y + 40, circle_x[colNum], circle_y[colNum])
        if distance < 60:
           character_alive = False 
        
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
    global character_x, character_y, character_alive
    global circle_x, circle_y
    global score
    
    if (character_alive == True):
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
    else:
        # Check if the player clicked on the Play Again button
        if mouseX >= 300 and mouseX <= 500 and mouseY >= 400 and mouseY <= 450:
           character_alive = True
           score = 0
           circle_x = []
           circle_y = []
           character_x = 350
           character_y = 350
        
        
        
        
        
        
        
        
        
