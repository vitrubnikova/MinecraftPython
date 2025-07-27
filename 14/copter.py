import mcpi.minecraft as mc
import mcpi.block as block
import time
import random
import minecraftstuff as mcs

# Подключаемся к Minecraft
craft = mc.Minecraft.create()

'''
Форма квадрокоптера
qc - создается список объектов ShapeBlock, который описывает форму квадрокоптера
Каждый ShapeBlock указывает координаты и тип блока, который будет использован для создания квадрокоптера
'''
qc = [
    mcs.ShapeBlock(0, 0, 0, block.IRON_BLOCK.id),
    mcs.ShapeBlock(-1, 0, 1, block.IRON_BLOCK.id),
    mcs.ShapeBlock(-1, 0, -1, block.IRON_BLOCK.id),
    mcs.ShapeBlock(1, 0, 1, block.IRON_BLOCK.id),
    mcs.ShapeBlock(1, 0, -1, block.IRON_BLOCK.id),
    mcs.ShapeBlock(-1, -1, 1, block.GLOWSTONE_BLOCK.id),
    mcs.ShapeBlock(-1, -1, -1, block.GLOWSTONE_BLOCK.id),
    mcs.ShapeBlock(1, -1, 1, block.GLOWSTONE_BLOCK.id),
    mcs.ShapeBlock(1, -1, -1, block.GLOWSTONE_BLOCK.id),
    mcs.ShapeBlock(-1, 1, 1, block.DIAMOND_BLOCK.id),
    mcs.ShapeBlock(-1, 1, -1, block.DIAMOND_BLOCK.id),
    mcs.ShapeBlock(1, 1, 1, block.DIAMOND_BLOCK.id),
    mcs.ShapeBlock(1, 1, -1, block.DIAMOND_BLOCK.id)
]

# Получение позиции игрока и создание квадрокоптера
cor = craft.player.getTilePos()
cor = mc.Vec3(cor.x + 5, cor.y + 10, cor.z)

'''
Обращение к объекту MinecraftShape, который строит форму квадрокоптера на основе списка в указанных координатах
Этот объект управляет квадрокоптером в Minecraft
'''
qcShape = mcs.MinecraftShape(craft, cor, qc)

# Работа квадрокоптера
work = True

try:  # пробовать
    while work:
        # генерация случайного числа для направления по оси X (-1, 0 или 1)
        r1 = random.randint(-1, 1)
        # генерация случайного числа для направления по оси Z (-1, 0 или 1)
        r2 = random.randint(-1, 1)
        # проверка, что хотя бы одно из значений не равно нулю, и что работа продолжается
        if r1 != 0 or r2 != 0 and work:
            # цикл, который выполняет 10 шагов для движения квадрокоптера
            for i in range(10):
                time.sleep(0.5)  # задержка в полсекунды между шагами для замедления движения
                if not work:
                    break  # для выхода из цикла
                qcShape.moveBy(r1, 0, r2)  # перемещение квадрокоптера на случайное расстояние
except Exception as e:  # обработка ошибки
    print(f"Ошибка: {e}")

print("Скрипт завершен")
