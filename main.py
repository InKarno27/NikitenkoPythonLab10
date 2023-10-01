"""
Лабораторная 10 Вариант 9
Написать функцию, которая генерирует матрицу 5×5 и заполняет её случайными значениями и возвращает минимальное
и максимальное значения полученной матрицы.
"""

import random

def generate_and_find_min_max():
    # Создаем пустую матрицу 5x5
    matrix = [[0] * 5 for _ in range(5)]

    # Заполняем матрицу случайными значениями от 1 до 100
    for i in range(5):
        for j in range(5):
            matrix[i][j] = random.randint(1, 100)

    # Ищем минимальное и максимальное значения в матрице
    min_value = min(min(row) for row in matrix)
    max_value = max(max(row) for row in matrix)

    return matrix, min_value, max_value

# Вызываем функцию и получаем матрицу, минимальное и максимальное значения
matrix, min_val, max_val = generate_and_find_min_max()

# Выводим результаты
print("Сгенерированная матрица 5x5:")
for row in matrix:
    print(row)

print(f"Минимальное значение: {min_val}")
print(f"Максимальное значение: {max_val}")
