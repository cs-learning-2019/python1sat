# Python Beginner
# Shoot Them Circles
# Feb 12, 2022

########## HOMEWORK #############
"""
1) Add a main menu to the game (hint: I already showed you how to make the game over screen)
Note: You do not have to have music or picture for the main menu
"""

########## Next steps to work on during class (NOT HOMEWORK) #############
"""
5) Talk about the bug with the spawn rate. Note I already fixed it in the code
6) Add ability to move diagonally
"""

# Some variables for the character
character_x = 350
character_y = 350
character_speed = 5
character_alive = True  # or this could be False
character_direction = "left" # The other options are "right", "up" and "down"

# Some variables for the circles
circle_x = []
circle_y = []
spawn_timer = 0

# Other variables
score = 0
first_time = True

add_library('minim')

def setup():
    global bad_guy
    global kirby_up
    global kirby_down
    global kirby_left
    global kirby_right
    global minim
    
    size(800, 800)
    
    # Load some images
    bad_guy = loadImage("bad.PNG")
    kirby_up = loadImage("kirby-up.jpg")
    kirby_down = loadImage("kirby-down.jpg")
    kirby_left = loadImage("kirby-left.jpg")
    kirby_right = loadImage("kirby-right.jpg")
    
    # Do some minim stuff
    minim = Minim(this)
    
    # Play sound effect
    minim.loadFile("Deep Logic.wav").loop()    
    
def draw():
    global minim
    global first_time
    
    if (character_alive == True):
        playGame()
    else:
        if first_time == True:
            minim.stop()
            minim.loadFile("End Game.wav").loop()
            first_time = False
        gameOver()

def gameOver():
    # Clear the game screen
    background(120, 120, 120)
    
    # Draw the game over text
    pushStyle()
    textAlign(CENTER)
    fill(255, 0, 0)
    font = loadFont("BookmanOldStyle-Italic-48.vlw")
    textFont(font)
    textSize(70)
    text("Game Over", 400, 130)
    popStyle()
    
    # Draw the score text
    pushStyle()
    textAlign(CENTER)
    fill(0, 0, 255)
    font = loadFont("ColonnaMT-48.vlw")
    textFont(font)
    textSize(40)
    text("Your score is: " + str(score), 400, 210)
    popStyle()
    
    # Draw the score text
    pushStyle()
    textAlign(CENTER)
    textSize(40)
    fill(0, 255, 0)
    if score > 20:
        text("You are a pro", 400, 300)
    elif score > 10:
        text("You are good", 400, 300)
    else:
        text("You need practice", 400, 300)
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
    global character_direction
    global kirby_up
    global kirby_down
    global kirby_left
    global kirby_right
    global circle_x, circle_y, spawn_timer
    global score
    global bad_guy
    
    # Clear the previous frame (draw the background)
    background(132, 188, 242)
    
    # Draw the character (Kirby)
    if (character_alive == True):
        if character_direction == "left":
            image(kirby_left, character_x, character_y, 80, 80)
        elif character_direction == "right":
            image(kirby_right, character_x, character_y, 80, 80)
        elif character_direction == "up":
            image(kirby_up, character_x, character_y, 80, 80)
        elif character_direction == "down":
            image(kirby_down, character_x, character_y, 80, 80)
    
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
    
    # Determine the spawn rate
    rate = 45
    if score > 30:
        rate = 10
    elif score > 20:
        rate = 20
    elif score > 10:
        rate = 35
    elif score > 5:
        rate = 40
    else:
        rate = 45
    
    # Spawn new circle
    spawn_timer = spawn_timer + 1
    if spawn_timer >= rate:
        spawn_timer = 0
        random_x = int(random(0, 800))
        random_y = int(random(0, 800))
        character_center_x = character_x + 40
        character_center_y = character_y + 40
        distance = dist(random_x, random_y, character_center_x, character_center_y)
        if (distance > 120):
            circle_x.append(random_x)
            circle_y.append(random_y)
    
    # Draw the circles (bad guy)
    for colNum in range(len(circle_x)):
        pushStyle()
        fill(255, 0, 0)
        stroke(255, 141, 0)
        strokeWeight(3)
        image(bad_guy, circle_x[colNum] - 50, circle_y[colNum] - 50, 70, 70)
        popStyle()
    
    # Get speed of the circles
    if score > 20:
        s = 3
    elif score > 10:
        s = 2
    else:
        s = 1
    
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
        new_x = circle_x[colNum] + difference_x * s
        new_y = circle_y[colNum] + difference_y * s
        
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
    global character_direction
    
    # Move up
    if key == "w" or key == "W":
        character_direction = "up"
        character_y = character_y - character_speed
        # We also need to check if the character went through the top wall
        if character_y < 0:
            character_y = 0
    # Move right
    elif key == "d" or key == "D":
        character_direction = "right"
        character_x = character_x + character_speed
        # We also need to check if the character went through the right wall
        if character_x > 720:
            character_x = 720
    # Move left
    elif key == "a" or key == "A":
        character_direction = "left"
        character_x = character_x - character_speed
        # We also need to check if the character went through the left wall
        if character_x < 0:
            character_x = 0
    # Move down
    elif key == "s" or key == "S":
        character_direction = "down"
        character_y = character_y + character_speed
        # We also need to check if the character went through the top wall
        if character_y > 720:
            character_y = 720

def mousePressed():
    global character_x, character_y, character_alive
    global circle_x, circle_y
    global score
    global minim
    global first_time
    
    if (character_alive == True):
        # Draw the laser
        pushStyle()
        stroke(245, 62, 236)
        strokeWeight(4)
        line(mouseX, mouseY, character_x + 40, character_y + 40)
        popStyle()
        
        # Play sound effect
        minim.loadFile("Score.wav").play()
        
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
           first_time = True
           minim.stop()  # Stop the end game song
           minim.loadFile("Deep Logic.wav").loop()
        
        
        
        
        
        
        
        
        
