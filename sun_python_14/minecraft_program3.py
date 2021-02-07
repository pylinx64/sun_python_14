from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for y in range(77, 200):
	time.sleep(0.2)
	id_block = random.randint(0, 100) 				# в игре в интвенторе 
	mc.setBlock(x, y, z, id_block)
