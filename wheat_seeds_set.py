"""Set wheat seeds.
- ref: http://konbu-coupe.sakura.ne.jp/recipe/recipe/1/0/295.html
"""
from mcpi.minecraft import Minecraft
import mcpi.block as block


def main():
    # connect to minecraft
    mc = Minecraft.create()
    mc.postToChat("Wheat init...")

    # get player's position
    x, y, z = mc.player.getPos()

    # set Wheet Seeds
    mc.setBlocks(
        x + 1,
        y + 1,
        z + 1,
        x + 3,
        y + 1,
        z + 3,
        # NOTE: WHEAT_SEEDS_ID=295
        block.WHEAT_SEEDS.id
    )


if __name__ == "__main__":
    main()
