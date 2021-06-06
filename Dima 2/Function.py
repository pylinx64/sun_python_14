import turtle, random

colors=['#FF9D00', '#A161EC', '#FF000A', '#0D00FF', '#00FF0A', '#00F3FF']

turtle.bgcolor('black')

t=turtle.Pen()

def side(i, m, n):
	t.pencolor(colors[n])
	t.forward(m)
	t.left(i)

lenth = 34
angle = 17
while True:
	n = random.randint(0, 5)
	side(angle, lenth, n)

turtle.done()
