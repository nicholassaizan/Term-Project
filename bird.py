# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import math,random


def bird(x,y,size,vel,d,canvas,data):
    xpos = x
    ypos = y
    size = size
    velocity = vel
    dir = d
    flappingspeedmultiplier = 2
    time = data.time*flappingspeedmultiplier
    bobbing = size*0.6*math.cos(time-math.pi*(3/2))
    drawBody(xpos,ypos,size,dir,time,bobbing,canvas,data)
    drawWing(xpos,ypos,size,dir,time,bobbing,canvas,data)
def drawBody(xpos,ypos,size,dir,time,bobbing,canvas,data):
    body0x=xpos+size*1.5*dir
    body0y=ypos+size*-0.75+bobbing
    body1x=xpos+size*2.75*dir
    body1y=ypos+size*-0.7+bobbing
    body2x=xpos+size*3.25*dir
    body2y=ypos+size*0+bobbing
    body3x=xpos+size*2.75*dir
    body3y=ypos+size*0+bobbing
    body4x=xpos+size*0*dir
    body4y=ypos+size*1+bobbing
    body5x=xpos+size*-3.6*dir
    body5y=(ypos+size*0.2+
        size*0.5*math.cos(time-math.pi*(3.25/2)))
    body6x=xpos+size*-5.5*dir
    body6y=(ypos+size*0+
        size*0.4*math.cos(time-math.pi*(3.5/2)))
    body7x=xpos+size*-4*dir
    body7y=(ypos+size*-0.3+
        size*0.5*math.cos(time-math.pi*(3.25/2)))
    body8x=xpos+size*-2*dir
    body8y=ypos+size*-0.5+bobbing
    canvas.create_polygon(
        body0x,body0y,
        body1x,body1y,
        body2x,body2y,
        body3x,body3y,
        body4x,body4y,
        body5x,body5y,
        body6x,body6y,
        body7x,body7y,
        body8x,body8y,fill="black")
def drawWing(xpos,ypos,size,dir,time,bobbing,canvas,data):
    wing0x = xpos+size*1.5*dir
    wing0y = ypos+size*-0.75+bobbing
    wing1x = xpos+size*1.25*dir
    wing1y = ypos+size*1.5*math.cos(time-math.pi/16)
    wing2x = xpos+size*2.1*dir
    wing2y = ypos+size*3*math.cos(time-math.pi/7)
    wing3x = xpos+size*1*dir
    wing3y = ypos+size*4.6*math.cos(time-math.pi/4)
    wing4x = xpos+size*-2.6*dir
    wing4y = ypos+size*7.2*math.cos(time-math.pi/2.4)
    wing5x = xpos+size*-3.5*dir
    wing5y = ypos+size*6.5*math.cos(time-math.pi/2.6)
    wing6x = xpos+size*-1.5*dir
    wing6y = ypos+size*3.75*math.cos(time-math.pi/4)
    wing7x = xpos+size*-2.2*dir
    wing7y = ypos+size*2.1*math.cos(time-math.pi/16)
    wing8x = xpos+size*-2*dir
    wing8y = ypos+size*-0.5+bobbing
    canvas.create_polygon(
        wing0x,wing0y,
        wing1x,wing1y,
        wing2x,wing2y,
        wing3x,wing3y,
        wing4x,wing4y,
        wing5x,wing5y,
        wing6x,wing6y,
        wing7x,wing7y,
        wing8x,wing8y,fill='black')