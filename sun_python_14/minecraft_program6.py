from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()	
x = pos.x
y = pos.y - 1
z = pos.z 

w = 10		# размер по х
l = 20		# размер по z
block = 20

mc.setBlocks(x, y, z, 
		  x + w, y, z + l, block)

while True:
	if block == 20:
		block = 46
	elif block == 46:
		block = 51
	elif block == 51:
		block = 35
	else:
		block = 20
	time.sleep(0.1)
	mc.setBlocks(x, y, z, 
		  x + w, y, z + l, block)

