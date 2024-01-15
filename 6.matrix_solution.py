import numpy as np


def gauss_elimination(A, b):
    n = len(b)

    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск максимального элемента в текущем столбце
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Перестановка строк для улучшения устойчивости алгоритма
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Приведение матрицы к верхнетреугольному виду
        pivot = A[i][i]
        for k in range(i + 1, n):
            factor = A[k][i] / pivot
            b[k][0] -= factor * b[i][0]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i][0] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k][0] -= A[k][i] * x[i]

    return x


def tridiagonal_solver(A, b):
    x = np.linalg.solve(A, b)

    return x


A = [
    [-3, 4, -1, 0, 0, 0, 0],
    [1.8824, -4.015, 2.1176, 0, 0, 0, 0],
    [0, 1.8889, -4.015, 2.1111, 0, 0, 0],
    [0, 0, 1.8947, -4.015, 2.1053, 0, 0],
    [0, 0, 0, 1.9, -4.015, 2.1, 0],
    [0, 0, 0, 0, 1.9048, -4.015, 2.0952],
    [0, 0, 0, 0, 1, -4, 3.2],
]

b = [[0.15], [0.01], [0.01], [0.01], [0.01], [0.01], [0.3]]

# print(*tridiagonal_solver(A, b), sep = "\n")

print("Метод Гаусса:")
print(*gauss_elimination(A, b), sep="\n")
