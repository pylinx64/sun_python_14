from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

air = 0 


while True:
	block = random.randint(10,20)
	pos = mc.player.getTilePos()		# собирает координаты игрока
	x = pos.x
	y = pos.y
	z = pos.z
	time.sleep(0.1)
	mc.setBlock(x, y-1, z, block)
	
