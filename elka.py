import turtle

t = turtle.Pen()

def star(n):
	'''рисует звездочку'''	
	t.left(90)
	t.forward(3*n)
	t.color("orange", "yellow") # цвет карандаша, цвет заливки
	t.begin_fill()              # начало заливка
	t.left(126)
	for i in range(5):
		t.forward(n/5)
		t.right(144)
		t.forward(n/5)
		t.left(72)
	t.end_fill()                # конец заливки
	t.right(126)
	
def tree(d, s):
	'''рисует елочку'''
	if d <= 0: return				
	t.forward(s)
	tree(d-1, s*0.8)
	t.right(120)
	tree(d-3, s*0.5)
	t.right(120)
	tree(d-3, s*0.5)
	t.right(120)
	t.backward(s)
	
t.speed('fastest')
star(100)
t.backward(100*4.8)
t.color('dark green')
tree(20, 100)
turtle.done()    
		
