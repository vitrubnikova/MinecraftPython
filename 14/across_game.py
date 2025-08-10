import mcpi.minecraft as mc
import mcpi.block as block
import time

# Подключаемся к Minecraft
mc = mc.Minecraft.create()
pos = mc.player.getTilePos()

xp = pos.x
yp = pos.y + 50
zp = pos.z

# создание функции classics и спавн блоков
def classics(x, y, z):
    mc.setBlocks(x - 1, y - 1, z, x + 1, y - 1, z + 6, block.IRON_BLOCK.id)

    mc.setBlock(x, y - 1, z + 1, block.DIAMOND_BLOCK.id)
    mc.setBlock(x - 1, y - 1, z + 2, block.DIAMOND_BLOCK.id)
    mc.setBlock(x + 1, y - 1, z + 2, block.DIAMOND_BLOCK.id)
    mc.setBlock(x, y - 1, z + 3, block.DIAMOND_BLOCK.id)
    mc.setBlock(x - 1, y - 1, z + 4, block.DIAMOND_BLOCK.id)
    mc.setBlock(x + 1, y - 1, z + 4, block.DIAMOND_BLOCK.id)
    mc.setBlock(x, y - 1, z + 5, block.DIAMOND_BLOCK.id)

mc.player.setTilePos(xp, yp + 2, zp)  # игрок стоит над площадкой с классиками

classics(xp, yp, zp)

# добавление переменных
scores = 0
timer = 0
level = 1
diamonds = 7

# вывод в чат
mc.postToChat("Привет! Через 10 секунд начнется игра Классики!")
time.sleep(10)
mc.postToChat("Игра началась! Удачи!")

# запуск игры с помощью бесконечного цикла
while True:
    time.sleep(1)
    # увеличение таймера на единицу
    timer += 1

    pos = mc.player.getTilePos()

    x = pos.x
    y = pos.y - 1
    z = pos.z

    b = mc.getBlock(x, y, z)

    # если игрок касается блока DIAMOND
    if b == block.DIAMOND_BLOCK.id:
        # к счету прибавляется единица
        scores += 1
        # уменьшается количество алмазных блоков
        diamonds -= 1
        # создается железный блок
        mc.setBlock(x, y, z, block.IRON_BLOCK.id)
        # вывод в чат
        mc.postToChat("Scores: " + str(scores))
        mc.postToChat(f"Timer: {timer}")
        mc.postToChat("Level: ")
        mc.postToChat("Diamonds: ")

    # если игрок касается блока IRON
    if b == block.IRON_BLOCK.id:
        # из счета вычитается 3
        scores -= 3
        # создание блока с воздухом
        mc.setBlock(x, y, z, block.AIR.id)
        # вывод в чат
        mc.postToChat("Scores: " + str(scores))
        mc.postToChat(f"Timer: {timer}")
        mc.postToChat("Level: ")
        mc.postToChat("Diamonds: ")

    # если алмазных блоков не осталось
    if diamonds < 1:
        diamonds = 7
        level += 1
        # вывод в чат
        mc.postToChat("Scores: " + str(scores))
        mc.postToChat(f"Timer: {timer}")
        mc.postToChat(f"Level: {level}")
        classics(x, y, z)

    # условие, чтобы закончить игру (например, по сравнению с высотой игрока)
    if y < yp - 1:
        # yp = 50
        # у = касание блока
        # касание блока = высота игрока - 1
        # высота игрока = 52
        # если 51 < 49
        mc.postToChat("Total:")
        mc.postToChat("Scores: " + str(scores))
        mc.postToChat(f"Timer: {timer}")
        mc.postToChat("Level: " + str(level))
        mc.setBlocks(xp - 1, yp - 1, zp, xp + 1, yp - 1, zp + 6, block.AIR.id)
        mc.postToChat("GG")
        # выход из цикла
        break
