# Focus Learning: Python Level 1
# Text, Images and Sounds in Processing
# Kavan Lam
# Oct 3, 2020

# You can get sound effects free from here http://soundbible.com/
# Tell Processing we want to uses the minim library
add_library("minim")

def setup():
    global font1
    global sunrise_pic
    global dog_pic
    global minim
    global monkey_sound
    
    size(900, 600)
    font1 = loadFont("BodoniMT-Italic-48.vlw")
    
    # Here we load a picture. The pictures should be in .jpg or .png format.
    # Also do not forget to go to sketch >> Add file first
    sunrise_pic = loadImage("sunrise.jpg")  
    dog_pic = loadImage("dog.jpg") 
    
    minim = Minim(this)  # store a dvd player in to the minim variable
    monkey_sound = minim.loadFile("monkey.mp3")
    
    # .loop will replay the sound when it is finished
    # .play will only play the sound from start to finish one time
    monkey_sound.loop() 
     
    
def draw():
    pushStyle()
    fill(255, 0, 0)
    textFont(font1)
    textSize(90)
    text("Hello", 50, 100)
    popStyle()
    
    pushStyle()
    image(sunrise_pic, 300, 300, 200, 200)
    image(dog_pic, 600, 300, 200, 200)
    popStyle()
    
