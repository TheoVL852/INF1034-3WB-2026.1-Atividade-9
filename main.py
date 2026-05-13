from turtle import *
import random
from time import sleep

t = Turtle()
t.speed(0)
colormode(255)
def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#Primeiro desenho

def drawSquare(t,size,r):
    t.pd()
    t.color(randomColor())
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(r): #pode mudar o numero pra ficar mais brabo
        t.fd(size)
        t.right(90)
    t.end_fill()
    t.pu()

def drawFractal(t, size ,r, step=50):
    if size == 0:
        return
    t.pu()
    t.fd(size)
    t.lt(20)
    t.pd()
    drawSquare(t,size,r)
    drawFractal(t,size-1,r,step)

t.pu()
t.goto(-250,100)
t.pd()

drawFractal(t,200,3)
t.clear()
#segundo desenho
t.pu()
t.rt(45)
t.goto(-300,250)
t.pd()
drawFractal(t,200,1)
sleep(2)
t.clear()
#terceiro
t.pu()
t.rt(45)
t.goto(-250,-250)
t.pd()
drawFractal(t,100,4)



mainloop()