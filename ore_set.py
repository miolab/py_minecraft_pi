"""Set various types of ore blocks.
"""
from mcpi.minecraft import Minecraft
import mcpi.block as block


def main():
    # connect to minecraft
    mc = Minecraft.create()
    mc.postToChat("Ore blocks init...")

    # get player's position
    x, y, z = mc.player.getPos()

    # set IRON block
    mc.setBlocks(
        x + 1,
        y + 0,
        z + 1,
        x + 3,
        y + 0,
        z + 3,
        # 42
        block.IRON_BLOCK.id
    )

    # set GOLD block
    mc.setBlocks(
        x + 1,
        y + 1,
        z + 1,
        x + 3,
        y + 1,
        z + 3,
        # 41
        block.GOLD_BLOCK.id
    )

    # set DIAMOND block
    mc.setBlocks(
        x + 1,
        y + 2,
        z + 1,
        x + 3,
        y + 2,
        z + 3,
        # 57
        block.DIAMOND_BLOCK.id
    )

    # set Coal Ore block
    mc.setBlocks(
        x + 1,
        y + 3,
        z + 1,
        x + 4,
        y + 3,
        z + 4,
        # 16
        block.COAL_ORE.id
    )

    # set GRAVEL block
    mc.setBlocks(
        x + 1,
        y + 4,
        z + 1,
        x + 3,
        y + 4,
        z + 3,
        # 13
        block.GRAVEL.id
    )

    # set Sugar cane block
    mc.setBlocks(
        x + 1,
        y + 5,
        z + 1,
        x + 3,
        y + 5,
        z + 3,
        # 83
        block.SUGAR_CANE.id
    )

    # set CLAY block
    mc.setBlocks(
        x + 1,
        y + 6,
        z + 1,
        x + 3,
        y + 6,
        z + 3,
        # 82
        block.CLAY.id
    )

    # set FURNACE_INACTIVE block
    mc.setBlocks(
        x + 1,
        y + 7,
        z + 2,
        x + 3,
        y + 7,
        z + 2,
        # 61
        block.FURNACE_INACTIVE.id
    )


if __name__ == "__main__":
    main()
