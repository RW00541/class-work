x = 0

def setup():
    size(640, 480)
    background(135, 206, 255)
    
def draw():
    global x
    if x >= 640:
        x = 0
    x += 3
    #land
    fill(0, 128, 0)
    rect(0, height - 50, width, 50)
    #train
    fill(0)
    ellipse(
