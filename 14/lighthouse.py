import mcpi.minecraft as minecraft  # подключи библиотеку и назови ее minecraft
import mcpi.block as block

craft = minecraft.Minecraft.create()  # создали переменную, которая обращается к библиотеке, из библиотеки взяли объект и вызвали у него определенный метод
cor = craft.player.getTilePos()  # обращаемся к переменной, которая создает игру, через нее обращаемся к объекту игрока и получаем координаты игрока с помощью метода

x = cor.x
y = cor.y
z = cor.z

for i in range(5):
    # первая опора башни
    craft.setBlock(x + i, y + i, z, block.STONE.id)
    # вторая опора башни
    craft.setBlock(x + 10 + i, y + 4 - i, z, block.STONE.id)
    # третья опора башни
    craft.setBlock(x + 10 + i, y + 4 - i, z + 5, block.STONE.id)
    # четвертая опора башни
    craft.setBlock(x + i, y + i, z + 5, block.STONE.id)
    # площадка на высоте y + 5
    craft.setBlocks(x + 5, y + 5, z, x + 10, y + 5, z + 5, block.STONE.id)

# четыре опоры на высоте y + 5
for w in range(5):
    craft.setBlock(x + 5, y + 5 + w, z, block.STONE.id)
    craft.setBlock(x + 10, y + 5 + w, z, block.STONE.id)
    craft.setBlock(x + 5, y + 5 + w, z + 5, block.STONE.id)
    craft.setBlock(x + 10, y + 5 + w, z + 5, block.STONE.id)

# площадка на высоте y + 10
craft.setBlocks(x + 5, y + 10, z, x + 10, y + 10, z + 5, block.STONE.id)

# две опоры для третьей площадки-крыши
for i in range(3):
    craft.setBlock(x + 5 + i, y + 11 + i, z, block.STONE.id)
    craft.setBlock(x + 8 + i, y + 13 - i, z, block.STONE.id)

# третья площадка-крыша
craft.setBlocks(x + 7, y + 13, z, x + 8, y + 13, z + 5, block.STONE.id)

# две оставшиеся опоры от второй до третьей площадки
for i in range(3):
    craft.setBlock(x + 5 + i, y + 11 + i, z + 5, block.STONE.id)
    craft.setBlock(x + 8 + i, y + 13 - i, z + 5, block.STONE.id)

# куб из золотых и стеклянных блоков с центральным блоком из лавы в центре башни на второй площадке
craft.setBlocks(x + 7, y + 6, z + 2, x + 8, y + 6, z + 3, block.GOLD_BLOCK.id)
craft.setBlocks(x + 6, y + 7, z + 1, x + 9, y + 8, z + 4, block.GLASS.id)
craft.setBlocks(x + 7, y + 7, z + 2, x + 8, y + 8, z + 3, block.LAVA_FLOWING.id)
craft.setBlocks(x + 7, y + 9, z + 2, x + 8, y + 9, z + 3, block.GOLD_BLOCK.id)
