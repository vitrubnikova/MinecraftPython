import mcpi.minecraft as mc
import mcpi.block as block
import time

# Подключаемся к Minecraft
mc = mc.Minecraft.create()

# функция для создания машины
def car(x, y, z):
    # основа машины
    mc.setBlocks(x, y, z, x + 5, y, z + 1, 89)
    # колеса
    mc.setBlock(x + 1, y + 1, z, 89)
    mc.setBlock(x + 1, y + 1, z + 1, 89)
    mc.setBlock(x + 4, y + 1, z, 89)
    mc.setBlock(x + 4, y + 1, z + 1, 89)

# пауза 5 секунд перед стартом
time.sleep(5)

# получение стартовых координат игрока
cor = mc.player.getTilePos()
x = cor.x + 2
y = cor.y
z = cor.z

# бесконечное движение по квадрату
while True:
    # вправо
    for i in range(10):
        car(x, y, z)
        time.sleep(0.1)
        mc.setBlocks(x, y, z, x + 5, y + 1, z + 1, block.AIR.id)
        x += 1

    # вперед
    for i in range(10):
        car(x, y, z)
        time.sleep(0.1)
        mc.setBlocks(x, y, z, x + 5, y + 1, z + 1, block.AIR.id)
        # ?

    # влево
    for i in range(10):
        car(x, y, z)
        time.sleep(0.1)
        mc.setBlocks(x, y, z, x + 5, y + 1, z + 1, block.AIR.id)
        # ?

    # назад
    for i in range(10):
        car(x, y, z)
        time.sleep(0.1)
        mc.setBlocks(x, y, z, x + 5, y + 1, z + 1, block.AIR.id)
        # ?


