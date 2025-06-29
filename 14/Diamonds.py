import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# Подключаемся к Minecraft
craft = minecraft.Minecraft.create()

# Получаем начальные координаты игрока
s = craft.player.getTilePos()

# Флаги для работы игры
game = True

# Переменные для отслеживания очков и времени
points = 0
timer = 0
count = 0

# Перемещаем игрока вверх, но не так высоко
craft.player.setTilePos(s.x, 100, s.z)

# Создаем платформу из золотых блоков
craft.setBlocks(s.x - 10, 90, s.z - 10, s.x + 10, 90, s.z + 10, block.GOLD_BLOCK.id)

# Выводим инструкцию в чат
craft.postToChat("Платформа постепенно исчезает")
craft.postToChat("Твоя задача - набрать как можно больше очков, собирая алмазы")
craft.postToChat("Не стой на месте! платформа будет исчезать прямо под тобой")

# Задержка перед стартом игры
time.sleep(5)

while game:
    # Получаем позицию игрока
    pos = craft.player.getTilePos()

    # Проверяем блок под ногами
    brick = craft.getBlock(pos.x, pos.y - 1, pos.z)

    # Ждем 0.5 секунды
    time.sleep(0.5)

    # Если под игроком золотой блок, убираем его
    if brick == block.GOLD_BLOCK.id:
        craft.setBlocks(pos.x - 1, pos.y - 1, pos.z - 1, pos.x + 1, pos.y - 1, pos.z + 1, block.AIR.id)

    # Генерируем случайные координаты для алмазного блока
    xd = s.x + random.randint(-10, 10)
    yd = 91
    zd = s.z + random.randint(-10, 10)

    # Создаем алмазный блок
    craft.setBlock(xd, yd, zd, block.DIAMOND_BLOCK.id)

    # Проверяем, ударил ли игрок блок (ПКМ по блоку)
    events = craft.events.pollBlockHits()
    for e in events:
        if e.pos.x == xd and e.pos.y == yd and e.pos.z == zd:
            craft.setBlock(xd, yd, zd, block.AIR.id)
            points += 1
            craft.postToChat("Points: " + str(points))

    # Увеличиваем таймер
    count += 1
    if count == 2:
        timer += 1
        craft.postToChat("Time: " + str(timer))
        count = 0

    # Генерация случайных координат для динамита
    xt = s.x + random.randint(-10, 10)
    yt = 91
    zt = s.z + random.randint(-10, 10)

    # После 15 секунд начинается падение динамита
    if timer >= 15:
        craft.setBlock(xt, yt, zt, block.TNT.id)
        craft.setBlock(xt, yt + 1, zt, block.FIRE.id)

    # Если игрок упал ниже уровня 90, игра заканчивается
    if pos.y < 90:
        craft.postToChat("Игра окончена")
        craft.setBlocks(s.x - 10, 90, s.z - 10, s.x + 10, 90, s.z + 10, block.AIR.id)

    craft.postToChat("------------------Итоги---------------------")
    craft.postToChat("Набрано баллов: " + str(points))
    craft.postToChat("Сыграно секунд: " + str(timer))
    craft.postToChat("------------------------------------")

    # Поинтересоваться у игрока, хочет ли тот сыграть заново
    # добавить переменную с вопросом (например, "Вы хотите начать игру заново? (да/нет): "), которая будет ждать ответа игрока (с помощью функции input) и приводить введенные данные к нижнему регистру (с помщью метода lower)
    # добавить условие, если игрок ответил "да" или "yes" - вывести в чат "Игра возобновится через 5 секунд", добавить паузу в 5 сек с помощью time.sleep
    # задать начальные координаты игрока с помощью setTilePos и передать туда координаты из переменной s, при этом y будет фиксированным и равным 100
    # сделать площадку из золота (как в 24 строке)
    # обнулить переменные для отслеживания очков и времени (16-18 строки)
    # если игрок отвечает что-то другое - нужно закончить игру (выйти из цикла) и вывести в чат строку, например "До свидания!"
