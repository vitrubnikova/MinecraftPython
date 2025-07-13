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