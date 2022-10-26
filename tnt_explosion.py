"""Set explodable TNT blocks.

- When struck with a sword, it detonates.
- ref: https://gangannikki.hatenadiary.jp/entry/2019/04/27/000000
"""
from mcpi.minecraft import Minecraft

# connect to minecraft
mc = Minecraft.create()
mc.postToChat("TNT init...")

# get player's position
x, y, z = mc.player.getPos()

# set TNT block
mc.setBlocks(
    x + 1,
    y + 1,
    z + 1,
    x + 3,
    y + 3,
    z + 3,
    46,
    1
)
