x = 0

def setup():
    size(640, 480)
    background(135, 206, 255)
    
def draw():
    global x
    if x >= 640:
        x = 0
    x += 3
    background(135, 206, 255)
    #land
    fill(0, 128, 0)
    rect(0, height - 50, width, 50)
    #Station
    fill(255, 128, 0)
    rect(450, height -80, 200, 30)
    fill(200, 100, 150)
    rect(520, height -200, 120, 120)
    fill(0, 0, 255)
    triangle(480, height - 200, 640, height - 260, 640, height - 200)
    #Lights
    fill(0)
    rect(460, height - 160, 10, 80)
    fill(255,255,0)
    ellipse(465, height - 160, 25, 25)
    #Sun
    fill(255, 255, 0)
    ellipse(520, height - 400 , 100, 100)
    #train
    fill(0)
    noStroke()
    ellipse(x+ 15, height -63, 30, 30)
    ellipse(x + 45, height - 63, 30, 30)
    ellipse(x + 75, height - 63, 30, 30)
    ellipse(x + 105, height - 63, 30, 30)
    fill(0, 0, 128)
    rect(x, height -80, 120, 5)
    rect(x-5, height -80, 5, 20)
    rect(x+120, height -80, 5, 20)
    rect(x-4, height -120, 120, 40)
    triangle(x+115, height - 120, x + 140, height - 70, x + 115, height -70)
    #funnel
    rect(x+100, height - 140, 10, 40)
    ellipse(x+105, height - 140, 10, 10)
    #control center
    rect(x, height -160, 10, 60)
    rect(x + 40, height - 160, 10, 60)
    rect(x -10, height -160, 70, 10)
    #Design
    fill(255, 0, 0)
    rect(x - 3, height -90, 133, 5)
    rect(x +110, height - 120, 2, 30)
    rect(x + 90, height - 120, 2, 30)
    rect(x + 70, height - 120, 2, 30)
    rect(x + 50, height - 120, 2, 30)
    #Number
    rect(x + 25, height - 115, 2, 20)
    rect(x + 20, height - 115, 5, 2)
    rect(x + 20, height - 95, 12, 2)
    #Trailer
    fill(0)
    ellipse(x - 30, height - 63, 30, 30)
    ellipse(x - 60, height - 63, 30, 30)
    ellipse(x - 120, height - 63, 30, 30)
    ellipse(x - 150, height - 63, 30, 30)
    fill(0,0,255)
    rect(x -170 ,height -80, 160, 5)
    rect(x - 165, height - 131, 150, 50)
    fill(0)
    rect(x-165, height -85, 150, 5)
    rect(x -165, height - 130, 5, 50)
    rect(x - 20, height - 130, 5, 50)
    triangle(x- 175, height - 130, x - 90, height - 180, x - 5, height - 130)
    #window
    fill(255)
    rect(x - 155,height -125, 130, 20)
    fill(0)
    rect(x - 130, height - 125, 5, 20)
    rect(x - 95, height - 125, 5, 20)
    rect(x - 60, height - 125, 5, 20)
    #Connector
    fill(0)
    rect(x - 10, height - 80, 8, 5)
    
    
