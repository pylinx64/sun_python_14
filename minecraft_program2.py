from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

x = 0						# в игре координаты - f3
y = 0
z = 0
id_block = 0 				# в игре в интвенторе 

for y in range(150, 1, -1):
	mc.setBlock(x, y, z, id_block)



