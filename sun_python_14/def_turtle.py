import turtle, random

colors=['#FFFFFF', '#00FF37', '#00F3FF']

turtle.bgcolor('black')

t=turtle.Pen()

def side(i, m, n):
	t.pencolor(colors[n])
	t.forward(m)
	t.left(i)

lenth = 100	# длина 
angle = 121	# градусы
while True:
	n = random.randint(0, 2)
	side(angle, lenth, n)


# останавливает программу
turtle.done()
