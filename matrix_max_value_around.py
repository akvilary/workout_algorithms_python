"""
Нужно найти самый оптимальный алгоритм
Задача:
    1) Есть матрица заполненная целыми числами (могут дублироваться, быть неуникальными).
    Матрица может быть любой длины и ширины:
        Может быть как 3 на 3, так и 10 на 2, или любой другой.
    2) Выбирается любая координата.
    3) Нужно найти максимальное значение среди соседних координат, исключая переданную координату.
"""

__author__ = 'https://github.com/akvilary'

from typing import List


def main(matrix: List[list], coordinates: tuple) -> int:
    """
    Суть решения:
        1) Найти максимальные координаты матрицы
        2) Получить все возможные прилегающие координаты:
            - отнимая единицу в координатах от строки и колонки, но не выходя за предел матрицы
            - прибавляя единицу в координатах от строки и колонки, но не выходя за предел матрицы
        3) Найти максимальное значение среди значений по полученным координатам
    """
    max_value = None

    rows_size = len(matrix)
    columns_size = len(matrix[0])
    if rows_size > 0 and columns_size > 0:
        # Получим границы матрицы
        min_coordinate = 0  # min_row, min_column
        max_row_coordinate = rows_size - 1
        max_column_coordinate = columns_size - 1

        # Получим область поиска
        type_index_map = {'row': 0, 'column': 1}
        get_coordinate = lambda _type: coordinates[type_index_map[_type]]
        get_start = lambda _type: get_coordinate(_type) - 1
        get_end = lambda _type: get_coordinate(_type) + 1
        search = {
            'start_row': start_row
            if ((start_row := get_start('row')) > min_coordinate)
            else min_coordinate,
            'start_column': start_column
            if ((start_column := get_start('column')) > min_coordinate)
            else min_coordinate,
            'end_row': end_row
            if ((end_row := get_end('row')) < max_row_coordinate)
            else max_row_coordinate,
            'end_column': end_column
            if ((end_column := get_end('column')) < max_column_coordinate)
            else max_column_coordinate,
        }

        # Вычислим максимальное значение по зоне поиска, кроме текущей координаты.
        # При любых размерах матрицы будет от 4 до 9 итераций (1 из них пропускаем)
        for row in range(search['start_row'], search['end_row'] + 1):
            for column in range(search['start_column'], search['end_column'] + 1):
                # пропускаем текущую координату
                if (row, column) == coordinates:
                    continue

                if max_value is None:
                    max_value = matrix[row][column]
                else:
                    max_value = (
                        matrix[row][column] if matrix[row][column] > max_value else max_value
                    )

    return max_value


if __name__ == '__main__':
    matrix = [
        [3, 8, 2],  # координаты ((0,0), (0,1), (0,2))
        [2, 3, 7],  # координаты ((1,0), (1,1), (1,2))
        [4, 9, 1],  # координаты ((2,0), (2,1), (2,2))
    ]
    coordinates = (1, 2)
    result = main(matrix, coordinates)
    print(result)
    print('finished')
