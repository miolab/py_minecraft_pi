"""Set wheat area.
- ref: http://konbu-coupe.sakura.ne.jp/recipe/recipe/1/0/296.html
"""
from mcpi.minecraft import Minecraft
import mcpi.block as block


def main():
    # connect to minecraft
    mc = Minecraft.create()
    mc.postToChat("Wheat init...")

    # get player's position
    x, y, z = mc.player.getPos()

    # set WHEAT
    mc.setBlocks(
        x + 1,
        y + 1,
        z + 1,
        x + 3,
        y + 1,
        z + 3,
        # NOTE: WHEAT_ID=296
        block.WHEAT.id
    )


if __name__ == "__main__":
    main()
