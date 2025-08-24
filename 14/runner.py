import mcpi.minecraft as mc
import mcpi.block as b
import time
import random


mc = mc.Minecraft.create()
blocks = [
    b.AIR.id,
    b.ICE.id,
    b.GOLD_BLOCK.id,
    b.OBSIDIAN.id
]

game_running = False
scores = 0
timer = 0
count = 0
start_x = 0
x = 0
y = 200
z = 0


# создание стартовой платформы изо льда и телепортация игрока
def setup_platform(x, y, z):
    # тело функции
    mc.player.setTilePos(x, y + 5, z)
    mc.setBlocks(x - 5, y, z - 5, x + 5, y, z + 5, b.ICE.id)  # платформа изо льда


# очистка ранее сгенерированных блоков
def clear_generated_blocks(start_x, y, z, count):
    # тело функции
    for offset in range(count + 20):  # увеличение диапазона для полной очистки
        for i in range(-2, 3):  # 5 блоков в ширину
            mc.setBlock(start_x + offset, y, z + i, b.AIR.id)


# запуск игры (строится платформа, устанавливаются начальные параметры)
def game_start(x, y, z):
    # тело функции
    global game_running, scores, timer, count, start_x
    setup_platform(x, y, z)
    mc.postToChat("Игра начинается через 10 секунд. Вы готовы, дети?)")
    time.sleep(10)
    mc.postToChat("Игра началась!")
    game_running = True
    scores = 0
    timer = 0
    count = 0  # сброс счетчика для генерации платформы
    start_x = x + 5  # начальная позиция для генерации платформы

# создание случайных блоков с разрывами
def generate_blocks(start_x, y, z, count):
    # тело функции
    for i in range(-2, 3):  # 5 блоков в ширину
        if random.random() < 0.4:  # 40% шанс оставить пустоту для паркур-эффекта
            mc.setBlock(start_x + count, y, z + i, b.AIR.id)
        else:
            block_choice = random.choice(blocks[1:])  # выбор случайного блока (лед, золото или обсидиан)
            '''
            СЛАЙСЫ (срезы)
            синтаксис:
            list[start:stop:step]
            list - список
            start - индекс начала слайса (включительно)
            stop - индекс конца слайса (не включается)
            step - шаг (может быть отрицательным)
            '''
            mc.setBlock(start_x + count, y, z + i, block_choice)

# очистка блоков и перезапуск игры с новой платформой
def game_over(current_x, y, z):
    # тело функции
    pass  # убрать
    '''
    ДЗ
    обратиться к глобальным переменным game_running, scores, timer, count, start_x
    вывести в чат сообщение о том, что игра окончена
    вывести в чат разделитель между сообщениями (типа такого "------------------")
    '''



