# Focus Learning: Python Level 1
# Shoot Them Circles
# Kavan Lam
# May 29, 2021

# Steps
# 1) Setup the screen  [Done]
# 2) Create the character and allow it to move using WASD and ensure that the character can't leave the screen [Done]
# 3) Allow the character to shoot red lasers [Done]
# 4) Create the cirlce (bad guys) they will spawn randomly  [Done]
# 5) Make the circles move towards the character [Done]
# 6) The character needs to die when one circle overlaps it ][Done]
# 7) The cicles need to die when we click on them [Done]
# 8) We need to replace the sqaure with an actual character [Done]
# 9) Make the character change directions [Done]
# 10) Display some score [Done]

character_x = 400
character_y = 350
character_size = 100
character_speed = 10
character_is_dead = False
character_pics = []
use_pic = 0
score = 0

circle_x = []
circle_y = []
circle_r = []
circle_g = []
circle_b = []
timer_countdown = 30

def setup():
    global character_pics
    size(900, 900)
    character_pics.append(loadImage("kirby-down.jpg"))  # index 0
    character_pics.append(loadImage("kirby-left.jpg"))  # index 1
    character_pics.append(loadImage("kirby-right.jpg")) # index 2
    character_pics.append(loadImage("kirby-up.jpg"))    # index 3
    
def draw():
    global character_x
    global character_y
    global character_size
    global character_pics
    global character_is_dead
    global use_pic
    global score
    global circle_x
    global circle_y
    global circle_r
    global circle_g
    global circle_b
    global timer_countdown
    
    # Clear the previous frame
    background(255, 255, 255)
    
    if character_is_dead == False:
        # Draw the character
        pushStyle()
        image(character_pics[use_pic], character_x, character_y, character_size, character_size)
        popStyle()
        
        # Draw the score
        pushStyle()
        fill(0, 255, 0)
        textSize(30)
        text(score, 30, 40)
        popStyle()
        
        # Spawn a circle
        if timer_countdown <= 0:
            x = int(random(0, 900))
            y = int(random(0, 900))
            r = int(random(0, 255))
            g = int(random(0, 255))
            b = int(random(0, 255))
            
            circle_x.append(x)
            circle_y.append(y)
            circle_r.append(r)
            circle_g.append(g)
            circle_b.append(b)
            
            timer_countdown = 30
        else:
            timer_countdown = timer_countdown - 1
        
        # Draw the circle
        for index in range(0, len(circle_x)):
            pushStyle()
            fill(circle_r[index], circle_g[index], circle_b[index], 50)
            ellipse(circle_x[index], circle_y[index], 50, 50)
            popStyle()
        
        # Move the circles towards the character
        for index in range(0, len(circle_x)):
            diff_x = character_x + (character_size / 2) - circle_x[index]
            diff_y = character_y + (character_size / 2) - circle_y[index]
            
            if diff_x > 0:
                diff_x = 1
            elif diff_x < 0:
                diff_x = -1
            else:
                diff_x = 0
                
            if diff_y > 0:
                diff_y = 1
            elif diff_y < 0:
                diff_y = -1
            else:
                diff_y = 0
            
            circle_x[index] = circle_x[index] + diff_x
            circle_y[index] = circle_y[index] + diff_y
            
        # Detect if any one of the circles touch the character (detect if the character dies)
        for index in range(0, len(circle_x)):
            x = circle_x[index]
            y = circle_y[index]
            A = character_x + 50
            B = character_y + 50
            result = distance(x, y, A, B)
            if result <= 60:
                character_is_dead = True
    
def mousePressed():
    global character_x
    global character_y
    global circle_x
    global circle_y
    global circle_r
    global circle_g
    global circle_b
    global score
    
    # Draw the laser
    pushStyle()
    stroke(255, 0, 0)
    strokeWeight(5)
    line(character_x + (character_size / 2), character_y + (character_size / 2), mouseX, mouseY)
    popStyle()
    
    # Check which circles did not get hit by the laser
    temp_circle_x = []
    temp_circle_y = []
    temp_circle_r = []
    temp_circle_g = []
    temp_circle_b = []
    
    for index in range(0, len(circle_x)):
        d = distance(mouseX, mouseY, circle_x[index], circle_y[index])
        if d <= 50:  # This means the circle is dead
            score = score + 100
        else:  # This means the circle is not die
            temp_circle_x.append(circle_x[index])
            temp_circle_y.append(circle_y[index])
            temp_circle_r.append(circle_r[index])
            temp_circle_g.append(circle_g[index])
            temp_circle_b.append(circle_b[index])
    
    circle_x = temp_circle_x
    circle_y = temp_circle_y
    circle_r = temp_circle_r
    circle_g = temp_circle_g
    circle_b = temp_circle_b
    
            
def keyPressed():
    global character_x
    global character_y
    global character_size
    global character_speed
    global use_pic
    
    if key == "W" or key == "w":  # Move up
        use_pic = 3
        character_y = character_y - character_speed
        if character_y < 0:
            character_y = 0
    elif key == "D" or key == "d":  # Move right
        use_pic = 2
        character_x = character_x + character_speed
        if character_x > 800:
            character_x = 800
    elif key == "S" or key == "s":  # Move down
        use_pic = 0
        character_y = character_y + character_speed
        if character_y > 800:
            character_y = 800
    elif key == "A" or key == "a":  # Move left
        use_pic = 1
        character_x = character_x - character_speed
        if character_x < 0:
            character_x = 0    
            
def distance(x, y, A, B):
    temp1 = (x - A) ** 2
    temp2 = (y - B) ** 2
    temp3 = temp1 + temp2
    distance = sqrt(temp3)
    return distance

           
           
           
           
           
        
