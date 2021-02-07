from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0 
block = 46

pos = mc.player.getTilePos()	
x = pos.x + 1
y = pos.y + 1
z = pos.z + 1

# ставит дом по 6 координатам
mc.setBlocks(x, y, z, 
			x + 20, y + 10, z + 30, block)
mc.setBlocks(x+1, y+1, z+1, 
			x + 19, y + 9, z + 29, air)
