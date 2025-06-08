import mcpi.minecraft as minecraft
import mcpi.block as block

craft = minecraft.Minecraft.create()

# проверить, на каком блоке стоит игрок
while True:
    cor = craft.player.getTilePos()  # получения координат игрока
    block_under = craft.getBlock(cor.x, cor.y - 1, cor.z)  # получение ID блока под игроком

    # если блок под игроком золотой - вывести определенное сообщение
    if block_under == 41:  # золотой блок
        craft.postToChat("Ты стоишь на золоте")  # выводит сообщение в чат
