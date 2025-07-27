import mcpi.minecraft as mc
import mcpi.block as block
import time

# Подключаемся к Minecraft
mc = mc.Minecraft.create()

pos = mc.player.getTilePos()

trap1_x = pos.x + 5
trap2_x = pos.x + 10
trap3_x = pos.x + 15
trap4_x = pos.x + 20
# trap5_x = pos.x + 25

y = pos.y
z = pos.z

# Создание площадки для ловушек
mc.setBlocks(pos.x - 10, y - 1, z - 10, pos.x + 20, y - 1, z + 10, 2)
mc.setBlocks(pos.x - 10, y, z - 10, pos.x + 30, y + 5, z + 10, 0)

# Установка блоков-ловушек
mc.setBlock(trap1_x, y, z, 57)
mc.setBlock(trap2_x, y, z, 41)
mc.setBlock(trap3_x, y, z, 42)
mc.setBlock(trap4_x, y, z, 12)
# mc.setBlock(trap5_x, y, z, id)

while True:
    time.sleep(0.1)
    pos = mc.player.getTilePos()

    # ловушка 1 - падение вниз
    if trap1_x - 1 <= pos.x <= trap1_x + 1 and z - 1 <= pos.z <= z + 1 and pos.y == y:
        mc.setBlocks(trap1_x - 1, y, z - 1, trap1_x + 1, 0, z + 1, 0)
        time.sleep(5)
        mc.player.setTilePos(pos.x, 100, pos.z)

    # своя ловушка

    # ловушка 2 - ловушка с TNT и огнем
    if trap2_x - 1 <= pos.x <= trap2_x + 1 and z - 1 <= pos.z <= z + 1 and pos.y == y:
        mc.setBlocks(trap2_x - 2, y - 3, z - 2, trap2_x + 2, y + 1, z + 2, 7)
        mc.setBlocks(trap2_x - 1, y - 2, z - 1, trap2_x + 1, y + 1, z + 1, 0)
        mc.setBlocks(trap2_x - 1, y - 2, z - 1, trap2_x + 1, y - 2, z + 1, 46)
        mc.setBlocks(trap2_x - 1, y - 1, z - 1, trap2_x + 1, y - 1, z + 1, 51)
        time.sleep(5)
        mc.player.setTilePos(pos.x, 100, pos.z)

    # ловушка 3 - лава в яме
    if trap3_x - 1 <= pos.x <= trap3_x + 1 and z - 1 <= pos.z <= z + 1 and pos.y == y:
        mc.setBlocks(trap3_x - 2, y - 3, z - 2, trap3_x + 2, y + 1, z + 2, 7)
        mc.setBlocks(trap3_x - 1, y - 2, z - 1, trap3_x + 1, y + 1, z + 1, 0)
        mc.setBlocks(trap3_x - 1, y - 2, z - 1, trap3_x + 1, y - 2, z + 1, 10)
        time.sleep(5)
        mc.player.setTilePos(pos.x, 100, pos.z)

    # ловушка 4 - глубокий бассейн с водой
    if trap4_x - 1 <= pos.x <= trap4_x + 1 and z - 1 <= pos.z <= z + 1 and pos.y == y:
        mc.setBlocks(trap4_x - 2, y, z - 2, trap4_x + 2, y + 1, z + 2, 0)
        mc.setBlocks(trap4_x - 2, y - 6, z - 2, trap4_x + 2, y, z + 2, 9)
        mc.setBlocks(trap4_x - 3, y, z - 3, trap4_x + 3, y + 1, z + 3, 4)
        mc.setBlocks(trap4_x - 2, y, z - 2, trap4_x + 2, y + 1, z + 2, 9)
        time.sleep(5)
        mc.player.setTilePos(pos.x, 100, pos.z)


