import mcpi.minecraft as minecraft  # подключи библиотеку и назови ее minecraft


craft = minecraft.Minecraft.create()  # создали переменную, которая обращается к библиотеке, из библиотеки взяли объект и вызвали у него определенный метод
cor = craft.player.getTilePos()  # обращаемся к переменной, которая создает игру, через нее обращаемся к объекту игрока и получаем координаты игрока с помощью метода

# Списки для id блоков
d1 = [4, 4, 4, 4, 4]  # отвечает за строительство сплошного ряда блоков из булыжника
d2 = [4, 20, 4, 20, 4]  # строительство окон в стене
d3 = [4, 4, 0, 4, 4]  # создание входа в дом

# Строим первую стену дома
n = len(d1)  # ширина и длина дома
# Строим два первых ряда со входом
for j in range(2):
    for i in range(n):
        craft.setBlock(cor.x + i, cor.y + j, cor.z, d3[i])
        craft.setBlock(cor.x + i, cor.y + 2 + j, cor.z, d1[i])
# Строим ряд блоков с окнами
for i in range(n):
    craft.setBlock(cor.x + i, cor.y + 4, cor.z, d2[i])
    craft.setBlock(cor.x + i, cor.y + 7, cor.z, d2[i])
    craft.setBlock(cor.x + i, cor.y + 8, cor.z, d1[i])
# Строим два сплошных ряда блоков
for j in range(2):
    for i in range(n):
        craft.setBlock(cor.x + i, cor.y + j + n, cor.z, d1[i])


