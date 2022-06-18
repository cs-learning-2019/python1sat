# First Name, Last Name
# Dec 14, 2019
# Python 1: Semester 1 Final Project
# Clicky Game

# Add required libraries below
<------------------------------->

# Defining important variables below
score = <------------------------------->
time = 6000
player_x = 500
player_y = 10
speed = 3
direction = <---------------------->
game_finished = False
minim = Minim(this)
first_time = True

<------------------------------->
    # Need global to get access to variables from outside
    global minim

    # Create the screen the width=800 and length = 700
    <------------------------------->

    # Start playing the main song in a loop (Deep Logic.wav)
    <------------------------------->


<------------------------------->
    # Need global to get access to variables from outside
    global score
    global game_finished
    global first_time

    # Draw the background to clear the screen
    background(200, 0, 0)

    # Draw the game over screen if game is finished
    if game_finished == True:
        # Stop the main song and play the end song (End Game.wav)
        if first_time == True:
            minim.stop()
            <------------------------------->
            first_time = <------------------------------->

        # Display the player's score and Game Over text
        textSize(50)
        fill(255, 255, 0)
        text("Game Over!", 200, 100)
        text("Score: " + str(<------------------->), 200, 150)
    else:
        play_game()

def play_game():
    # Need global to get access to variables from outside
    global score
    global <------------------------------->
    global player_x
    global player_y
    global speed
    global direction
    global game_finished

    # Draw the bottom (score area)
    fill(0, 255, 0)
    rect(0, 600, 700, 200)

    # Draw the score and time
    textSize(50)
    fill(255, 255, 0)
    text("Score: " + str(<---------------->), 0, 50)
    text("Time : " + str(<---------------->), 0, 120)

    # Draw the moving yellow square
    rect(player_x, <-------------------->, 70, 70)

    # Change the player's y location for the next scene
    <------------------------------------------------>

    # Change the direction if needed
    if player_y >= 730:
        direction = <-------------->
    elif player_y <= 0:
        <-------------------------->

    # Change the speed depending on the time left
    if time < 1000:
        speed = 16
    elif time < 1500:
        speed = 14
    elif time < 2000:
        speed = 12
    elif time < 2500:
        speed = 11
    elif time < 3000:
        speed = 10
    elif time < 3500:
        speed = 9
    elif time < 4000:
        speed = 8
    elif time < 4500:
        speed = 6
    elif time < 5500:
        speed = 5
    elif time < 6000:
        speed = 3

    # Change the time and end the game if time is up
    time = time - 1
    if time <= 0:
        game_finished = <------------------------------->


<------------------------------->
    # Need global to get access to variables from outside
    global <---------------->
    global game_finished
    global player_y
    global minim

    # If game is already over then do not change the score
    if game_finished != <--------------->:
        if player_y >= 600:
            # Play the score sound effect (Score.wav)
            <------------------------------->

            # Increase the score by 1
            <------------------------------->
        else:
            # Decrease the score by 1
            <------------------------------->
