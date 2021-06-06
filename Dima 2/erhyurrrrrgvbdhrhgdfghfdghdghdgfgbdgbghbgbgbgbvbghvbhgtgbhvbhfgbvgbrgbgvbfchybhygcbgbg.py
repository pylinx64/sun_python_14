import turtle
import time

colors = ['red', 'lime', 'orange', '#7238A7', '#40EDCB', '#3BDF22']
t = turtle.Pen()
turtle.bgcolor('black')

t.pencolor(colors[1])
t.forward(560)
t.left(360)
t.pencolor(colors[2])
t.forward(560)
t.left(360)
t.forward(560)

t.circle(10660)


time.sleep(1)
