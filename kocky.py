import turtle
import random

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)

def posun():
    t.pu()
    t.setpos(random.randint(-300, 300), random.randint(-300, 300))
    t.seth(random.randint(0, 359))
    t.pd()

t = turtle.Turtle()
for i in range(10):
    posun()
    stvorec(30)
