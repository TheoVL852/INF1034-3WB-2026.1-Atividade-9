from turtle import *
import random

t = Turtle()
t.speed(0)
colormode(255)
def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


def drawSquare(t,size):
    t.pd()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(3): #pode mudar o numero pra ficar mais brabo
        t.fd(size)
        t.right(90)
    t.end_fill()
    t.pu()

def drawSquareFractal(t, size , step=50):
    if size == 0:
        return
    t.fd(size)
    t.lt(20)
    drawSquare(t,size)
    drawSquareFractal(t,size-1,step)

drawSquareFractal(t,100)

mainloop()