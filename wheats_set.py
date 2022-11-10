"""Set wheat blocks.
"""
from mcpi.minecraft import Minecraft
import mcpi.block as block


def main():
    # connect to minecraft
    mc = Minecraft.create()
    mc.postToChat("Wheat init...")

    # get player's position
    x, y, z = mc.player.getPos()

    # set TNT block
    mc.setBlocks(
        x + 1,
        y + 1,
        z + 1,
        x + 15,
        y + 1,
        z + 15,
        # WHEAT_ID=296
        block.WHEAT.id
    )


if __name__ == "__main__":
    main()
