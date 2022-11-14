"""Move momentary to the coordinates.

- ref: https://yasuda.cc/minecraft-location-teleport/
"""
from mcpi.minecraft import Minecraft

# NOTE: Must set the place coordinates you want to go.
x = 1
y = 1
z = 1


def main():
    # connect to minecraft
    mc = Minecraft.create()
    mc.postToChat("Prepare moving...")

    mc.player.setPos(x, y, z)
    mc.postToChat(
        f'Move to {mc.player.getPos()}'
    )


if __name__ == "__main__":
    main()
