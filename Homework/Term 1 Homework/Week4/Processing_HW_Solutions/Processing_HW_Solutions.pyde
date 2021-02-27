# Focus Learning: Python Level 1
# Images, text and sounds Processing Homework Solutions
# Kavan Lam
# Oct 9, 2020


# Question 1
"""
You can change the font size by using the textSize() function/command
"""

# Question 2
"""
We use push and pop style in order to isolate styling commands for certain objects.
If we do not use it then changing the strokeWeight for one object can effect the 
other objects drawn before it.
"""

# Question 3
"""
The play function will play the sound file once and when it ends that is it. The .loop()
function will also play the sound file but when it finishes it will rewind and play again.
"""

# Question 4
"""
The data folder holds all of your game pictures, font and sound files. We call these
the project assets. The data folder is important because that is where Processing will
always look in order to find stuff for your project.
"""

# Question 5
add_library("minim")
def setup():
    global img
    size(900, 600)
    img = loadImage("game_over.jpg")
    minim = Minim(this)
    song = minim.loadFile("End_Game.wav")
    song.loop()
    
def draw():
    image(img, 300, 300, 250, 250)
    
    
    
    
    
    
    
