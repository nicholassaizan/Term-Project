# Things to do:
#     seeds for trees
#     adding trees
#     making terrain
from tkinter import *
import random
import bird
import math
import tree1


def init(data):
    data.time = 0
    data.birds = []
    data.spawnbird = False
    data.timemultiplier = 4
    data.foregroundTrees = []
    data.backgroundTrees = []
    data.offsetX = 0
    data.offsetY = 0
    data.explored = data.width-data.offsetX
    data.groundlevel = 30
    data.step = 3
    data.moving=True
def mousePressed(event, data):
    pass
def keyPressed(event, data):
    key = event.keysym
    if key == 'Left' or key == 'Right':         
        gameMovementKeyPressed(key,data)
    if key == 'space':
        data.moving = not data.moving
def gameMovementKeyPressed(key,data):
    if key == 'Right': data.offsetX-= data.step
def timerFired(data):
    if data.moving==True:data.offsetX-=2
    data.time+=data.timerDelay/1000*data.timemultiplier
    data.spawnbird = random.choice([True]+[False]*3)
    print(random.randint(0,3))
    birdSpawning(data)
    foregroundTreeSpawning(0,0,data)
    backgroundTreeSpawning(100,10,data)
def birdSpawning(data):
    if data.spawnbird == True:
        size = random.randint(2,4)
        velocity = random.randint(60,70)/3*size
        direction = random.randint(0,1)
        if direction == 1: 
            xpos = 0
        else:
            direction = -1 
            xpos = data.width
        ypos = random.randint(10,data.height//3)
        initTime = data.time
        data.birds.append([xpos,ypos,size,velocity,direction,initTime])
def foregroundTreeSpawning(tinter,sizer,data):
    for i in range(data.explored):
        if otherForegroundTreeinRange(i,data) == False:
            randomx = random.randint(0,140)
            len = random.randint(100,170)-sizer
            seed=random.randint(0,100)
            data.foregroundTrees.append([i+randomx,data.height,len,tinter,seed])
def backgroundTreeSpawning(tinter,sizer,data):
    for i in range(data.explored):
        if otherBackgroundTreeinRange(i,data) == False:
            randomx = random.randint(0,140)
            len = random.randint(100,170)-sizer
            seed=random.randint(0,100)
            data.backgroundTrees.append([i+randomx,data.height,len,tinter,seed])
def otherForegroundTreeinRange(i,data):
    for t in data.foregroundTrees:
        if abs(t[0]-i)<150: return True
    return False
def otherBackgroundTreeinRange(i,data):
    for t in data.backgroundTrees:
        if abs(t[0]-i)<100: return True
    return False
def redrawAll(canvas, data):
    for b in data.birds:
        movement = (data.time-b[5])*b[3]*b[4]
        bird.bird(b[0]+movement,b[1],b[2],b[3],b[4],canvas,data)
    for t in data.backgroundTrees:
        #print('x=',t[0],' y=',t[1],' len=',t[2],' seed=',t[3])
        offsetX = data.offsetX
        tree1.tree(t[0]+offsetX,t[1],t[2],math.pi/2,t[4],t[3],canvas)
    for t in data.foregroundTrees:
        #print('x=',t[0],' y=',t[1],' len=',t[2],' seed=',t[3])
        offsetX = data.offsetX
        tree1.tree(t[0]+2*offsetX,t[1],t[2],math.pi/2,t[4],t[3],canvas)
    canvas.create_rectangle(0,data.height-20,data.width,data.height,fill='black')
    
    
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 25 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 700)