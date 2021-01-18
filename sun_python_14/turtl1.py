import turtle
import time

colors = ['red', 'lime', 'orange', '#7238A7', '#40EDCB', '#3BDF22']
t = turtle.Pen()
turtle.bgcolor('black')

t.pencolor(colors[1])
t.forward(50)
t.left(30)
t.pencolor(colors[2])
t.forward(50)
t.left(30)
t.forward(50)

t.circle(100)


time.sleep(100)
