from PIL import Image
import numpy as np
from memory_profiler import profile

from utils import (
    ant_step,
    ant_rotate,
    invert_cell
)


# Для получения информации об использовании памяти
# уберите комментарий в следующей строке
#@profile
def ant_path():
    # Размер стороны поля
    size = 1024

    # Создание поля
    field = np.zeros(
        (size, size),
        dtype=np.uint8
    )

    # Начальная позиция муравья
    x, y = size // 2, size // 2

    # Начальное направление муравья
    # (0 - вверх, 1 - вправо, 2 - вниз, 3 - влево)
    direction = 0

    def move_ant(
            ant_x: int,
            ant_y: int,
            ant_direction: int
    ) -> tuple[int, int, int]:
        """
        Перемещение муравья и инвертирование цвета клетки
        """

        # Инвертирование цвета клетки
        field[ant_x, ant_y] = invert_cell(
            field[ant_x, ant_y]
        )

        # Поворот муравья
        ant_direction = ant_rotate(
            field[ant_x, ant_y],
            ant_direction
        )

        # Перемещение муравья
        return ant_step(
            ant_x,
            ant_y,
            ant_direction
        )

    # Движение муравья до границы поля
    while 0 < x < size and 0 < y < size:
        x, y, direction = move_ant(x, y, direction)

    # Преобразование поля в изображение и его сохранение
    image = Image.fromarray((1 - field) * 255)
    image.save('ant_path.png')

    # Подсчет числа черных клеток на изображении
    black_pixels = np.sum(field)
    print(f"Число черных клеток: {black_pixels}")


if __name__ == '__main__':
    ant_path()
