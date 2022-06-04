# First Name, Last Name
# Dec 14, 2019
# Python 1: Semester 1 Final Project
# Flappy Block [Base Code]
 
# Add required libaries below (hint there is only one)
<----------------------------->

# Defining important variables below
minim = Minim(this)
first_time = <----------------------------->
game_finished = <----------------------------->
score = <----------------------------->
gravity = 10
bird_x = 200
bird_y = 200
flap_power = 100
wall_x = 910
wall_width = 100
wall_spacing = 200
wall_speed = 10
background_img = None
bird_img = None

def setup():
    # Need global to get access to variables from outside
    global minim
    global background_img
    global bird_img
    
    # Create the screen the width=600 and length = 900
    size(<----------------------------->, <----------------------------->)
    
    # Start playing the main song in a loop
    minim.loadFile(<----------------------------->).loop()
    
    # Load the background image (background.jpg)
    background_img = <----------------------------->
    
    # Load the bird image
    bird_img = loadImage(<----------------------------->)
    
def draw():
    # Need global to get access to variables from outside
    global game_finished
    global first_time
    global score
    global background_img
    
    # Draw the background to prepare to draw the next scene
    image(<----------------------------->, 0, 0, 900, 600)
    
    # Draw the game over screen if game is finished
    if game_finished == <----------------------------->:
        # Stop the main song and play the end song (End Game.wav)
        if first_time == True:
            minim.stop()
            <--------------------------------->
            first_time = <----------------------------->
        
        # Display the player's score and Game Over text
        textSize(50)
        fill(255, 255, 0)
        text("Game Over!", 290, 100)
        text("Score: " + str(<----------------------------->), 290, 150)
    else:
        play_game()

def play_game():
    # Need global to get access to variables from outside
    global bird_x 
    global bird_y
    global gravity
    global wall_x 
    global wall_width 
    global wall_spacing
    global wall_speed
    global bird_img
    global score
    global game_finished
    
    # Draw the score and time
    textSize(50)
    fill(255, 255, 0)
    text("Score: " + str(<----------------------------->), 0, 50)
    
    # Draw the bird
    image(bird_img, <----------------------------->, bird_y, 60, 60)
    
    # Draw the wall
    # Start with top part
    fill(255, 0, 0)
    rect(<----------------------------->, 0, 60, wall_width)
    # End with the bottom part
    rect(wall_x, wall_width + wall_spacing, 60, 600 - wall_width - wall_spacing)
    
    # Gravity will pull the bird down so we need to change the birds location by applying gravity
    bird_y = bird_y + <----------------------------->
    
    # Check to see if the bird died
    if (wall_x + 60 >= bird_x >= wall_x) or (wall_x + 60 >= bird_x + 60 >= wall_x):
        # First check if the bird hit the top wall
        if (wall_width >= bird_y >= 0) or (<--------------------> >= bird_y + 60 >= <---------------------->):
            game_finished = <----------------------------->
        # Now check if the bird hit the bottom wall    
        elif (600 >= bird_y >= wall_width + wall_spacing) or (600 >= bird_y + 60 >= wall_width + wall_spacing):
            game_finished = <----------------------------->
    elif <-----------> > 650 or bird_y < -100:
        game_finished = <----------------------------->
            
    # Change the wall's location for the next scene
    wall_x = wall_x - <----------------------------->
    
    # Check to see if the wall needs to be set back to the front
    if <-------------------------> <= -10:
        wall_x = 910
        # Also need to generate a random width for the wall between 30 and 370
        wall_width = <------------------------->
        # Also need to increase the score by one since the bird survived the wall and play a sound (Tick.wav)
        minim.loadFile(<----------------------------->).play()
        <----------Increase the score by one -------->
        
def keyPressed():
    # Need global to get access to variables from outside
    global game_finished
    global bird_y
    global minim
    global flap_power
    
    # If game is already over then do not play any sonuds or move the bird
    if <-------------------------> != True and key == <----------Space bar---------->:
        bird_y = bird_y - <---------Move the bird up with flap power-------->
