import turtle

colors = ['#C43CC9', '#0CFEE1', '#85FE0C', '#FDB529', '#29F5FD']
t = turtle.Pen()
t.speed(15)
turtle.bgcolor('black')

word = turtle.textinput(' ', 'Подсказка 2')

for x in range(1000):
	t.pencolor(colors[x%5])
	t.penup()
	t.forward(x * 10)
	t.pendown()
	t.write(word, font=("Minecraft Title Cyrillic Regular", int((x + 4) / 4)))
	t.left(56)
