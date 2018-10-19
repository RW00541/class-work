x = 0

def setup():
    size(640, 480)
    background(135, 206, 255)
#clouds
def draw():
    global x
    if x >= 640:
        x = 0
    x += 5
    background(135, 206, 255)
    noStroke()
    #clouds
    fill(255, 255, 0)
    ellipse(width*3/4, height/4, 100, 100)
    fill(255,255,255)
    ellipse(x, height/3, 50, 50)
    ellipse(x-20, height/3-25, 50, 50)
    ellipse(x-35, height/3, 50,50)
    #grass
    fill(0, 128, 0)
    rect(0, height-50, width, 50)
    #human
    fill(0, 0, 255)
    rect(x/2+0, height -75, 10, 25)
    rect(x/2+20, height -75, 10, 25)
    rect(x/2, height -80, 30, 5)
    fill(255,0,0)
    rect(x/2+5, height -120, 20, 40)
    rect(x/2 - 15, height -120, 60, 10)
    fill(255,244,189)
    ellipse(x /2 +15, height -133 ,25,25)
    fill(0)
    ellipse(x/2 +20, height -136, 5, 5)
    ellipse(x/2 +13, height -136, 5, 5)
    rect(x/2  , height - 146,40, 5)
    fill(0, 0, 255)
    rect(x/2, height - 160, 30, 15)
    #house
    fill(255, 140, 0)
    rect(400, height-200, 220, 150)
    fill(101, 67, 33)
    rect(400, height- 160, 50, 110)
    fill(255)
    rect(440, height- 120, 5, 5)
    fill(255, 0, 0)
    triangle(380, height-200, 510, height -300, 640, height -200)
