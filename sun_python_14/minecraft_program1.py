# Подключаемся к серверу
from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

while True:
	time.sleep(5)

	# Координаты
	x = random.randint(-200, 200)
	y = random.randint(50, 250)
	z = random.randint(-200, 200)

	# Перемещает 
	mc.player.setTilePos(x, y, z)
