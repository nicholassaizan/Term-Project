from tkinter import *
import math,random
# root = Tk()
# canvas = Canvas(root, width=1000, height=1000)
# canvas.pack()
def tree(x,y,len,angle,seed,tinter,canvas):
    minlen=30
    def rgbString(red, green, blue):
        if red > 255: red = 255
        if green > 255: green = 255
        if blue > 255: blue = 255
        return "#%02x%02x%02x" % (red, green, blue)
    def drawTree(x,y,len,angle,seed,tinter,canvas):
        random.seed(seed)
        newangle = angle + random.randint(-2,2)/180*math.pi #-5,5
        canvas.create_line(x,y,x+len*math.cos(newangle),y-len*math.sin(newangle),
            width=len/9,fill=rgbString(0+tinter,0+tinter,0+tinter))
        drawBranch(x+len*math.cos(newangle),y-len*math.sin(newangle),
            len*(4/5),newangle,seed,tinter,canvas)
    def drawBranch(x,y,len,angle,seed,tinter,canvas):
        newlen = len*6/random.randint(8,11) #8,11
        width=len/8
        if width<2: width+=1
        branches = random.randint(2,3) #2,3
        newangle = angle + random.randint(20,30)/180*math.pi #20,30
        canvas.create_line(x,y,x+len*math.cos(newangle),y-len*math.sin(newangle),
            width=width,fill=rgbString(0+tinter,0+tinter,0+tinter))
        if len>minlen:
            drawBranch(x+len*math.cos(newangle),y-len*math.sin(newangle),
            newlen*8/random.randint(7,9),newangle,seed,tinter,canvas) #7,9
        else: drawLeaf(x+len*math.cos(newangle),y-len*math.sin(newangle),
                        len,newangle,seed,tinter,canvas)
        
        newangle = angle + random.randint(-30,-20)/180*math.pi #-30,-20
        canvas.create_line(x,y,x+len*math.cos(newangle),y-len*math.sin(newangle),
            width=width,fill = rgbString(0+tinter,0+tinter,0+tinter))
        if len>minlen:
            drawBranch(x+len*math.cos(newangle),y-len*math.sin(newangle),
            newlen*8/random.randint(7,9),newangle,seed,tinter,canvas) #7,9
        else: drawLeaf(x+len*math.cos(newangle),y-len*math.sin(newangle),
                        len,newangle,seed,tinter,canvas)
        if branches == 3: 
            newangle = angle + random.randint(-15,15)/180*math.pi #-15,15
            canvas.create_line(x,y,
                x+len*math.cos(newangle),y-len*math.sin(newangle),width=width,
                    fill = rgbString(0+tinter,0+tinter,0+tinter))
            if len>minlen:
                drawBranch(x+len*math.cos(newangle),y-len*math.sin(newangle),
                newlen*8/random.randint(7,9),newangle,seed,tinter,canvas) #7,9
            else: drawLeaf(x+len*math.cos(newangle),y-len*math.sin(newangle),
                            len,newangle,seed,tinter,canvas)
    def drawLeaf(x,y,len,angle,seed,tinter,canvas):
        radius=random.randint(2,4) #2,4
        # color = random.choice([rgbString(216+tinter,72+tinter,48+tinter),
        #                         rgbString(240+tinter,144+tinter,72+tinter),
        #                         rgbString(240+tinter,168+tinter,96+tinter),
        #                         rgbString(240+tinter,192+tinter,96+tinter)])    
        # canvas.create_oval( x-radius,y-radius,x+radius,y+radius,fill=color)
        pass
    drawTree(x,y,len,angle,seed,tinter,canvas)
    # drawTree(500,900,160,math.pi/2,random.randint(0,100),canvas)
    # root.mainloop()