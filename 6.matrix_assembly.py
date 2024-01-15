import numpy as np


def conditions(h, n, matrix_a, matrix_b, x):
    matrix_a, matrix_b = start(h, matrix_a, matrix_b)
    matrix_a, matrix_b = middle(x, h, n, matrix_a, matrix_b)
    matrix_a, matrix_b = end(h, n, matrix_a, matrix_b)
    return matrix_a, matrix_b


def start(h, matrix_a, matrix_b):
    matrix_a[0, 0] = -3
    matrix_a[0, 1] = 4
    matrix_a[0, 2] = -1

    matrix_b[0] = 3 * h
    return matrix_a, matrix_b


def middle(x, h, n, matrix_a, matrix_b):
    for i in range(1, n):
        matrix_a[i][i - 1] = 2 - p(x[i]) * h
        matrix_a[i][i] = q() * 2 * h ** 2 - 4
        matrix_a[i][i + 1] = 2 + p(x[i]) * h

        matrix_b[i] = f() * 2 * h ** 2

    return matrix_a, matrix_b


def end(h, n, matrix_a, matrix_b):
    matrix_a[n][n - 2] = 1
    matrix_a[n][n - 1] = -4
    matrix_a[n][n] = 3 + 4 * h

    matrix_b[n] = 6 * h

    return matrix_a, matrix_b


def p(x):
    return 2 / x


def q():
    return -3


def f():
    return 2


def draw_matrix(matrix_a, matrix_b):
    for i in range(len(matrix_a)):
        x[i] = float("{:.2f}".format(x[i]))
        for j in range(len(matrix_a[i])):
            matrix_a[i][j] = float("{:.4f}".format(matrix_a[i][j]))

        matrix_b[i][0] = float("{:.2f}".format(matrix_b[i][0]))
        print(f"{(x[i]):.2f} {matrix_a[i]} {matrix_b[i]}")


a = 0.8
b = 1.1
e = 10 ** (-3)
h = 0.05

n = int((b - a) // h)  # 6

matrix_a = np.zeros((n + 1, n + 1))
matrix_b = np.zeros((n + 1, 1))

x = [i for i in np.arange(a, b, h)]
matrix_a, matrix_b = conditions(h, n, matrix_a, matrix_b, x)

draw_matrix(matrix_a, matrix_b)
