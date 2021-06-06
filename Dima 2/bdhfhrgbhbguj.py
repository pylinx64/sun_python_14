def sayHello():
	print('Hello')
	
sayHello()

def sum2(a, b):
	s = a + b
	return s
	
z=sum2(1, 2)
print(z)

def orange6(a, b, c):
	s = a / b + c
	return s

z=orange6(12, 6, 12)
print(z)

def exp(a, b):
	s = a ** b
	return s
	
res = exp(2, 3)
print(res)

import time
def test1(a, b):
	print('--------------#test1---------------------')
	et = time.time()
	res = exp(a, b)
	st = time.time()
	dt = st - et
	print('#time - ', dt)
	print('#result - ', res)
	
test1(100000, 100000)
