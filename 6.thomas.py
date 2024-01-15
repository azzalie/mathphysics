import numpy as np


# Функция создания первого краевого условия
def first_condition(A, b, x, h):
    # Вычисление коэффициентов для матрицы A
    y_0 = 2 * h * a_1() - 3 * b_1()
    y_1 = 4 * b_1()
    y_2 = -b_1()

    # Вычисление коэффициента для матрицы b
    answer = 2 * h * c_1()

    # Вывод первого ограничения
    print(f"{0}: ({y_0:.4f})y0 + ({y_1:.4f})y1 + ({y_2:.4f})y2 = {answer:.4f}")

    # Заполнение первой строки матрицы A
    A[0][0] = y_0
    A[0][1] = y_1
    A[0][2] = y_2

    # Заполнение первой строки матрицы b
    b[0][0] = answer

    # Возвращаем измененные матрицы A и b
    return A, b


# Функция создания средних условий
def middle_conditions(A, b, x, h):
    # Перебор основных уравнений
    for i in range(1, len(x) - 1):
        # Вычисление коэффициентов для матрицы A
        y_i_l = 2 - h * p(x[i])
        y_i = 2 * h ** 2 * q(x[i]) - 4
        y_i_r = h * p(x[i]) + 2

        # Вычисление коэффициента для матрицы b
        answer = 2 * h ** 2 * f(x[i])

        # Вывод первого ограничения
        print(f"{i}: ({y_i_l :.4f})y{i - 1} + ({y_i :.4f})y{i} + ({y_i_r :.4f})y{i + 1} = {answer:.4f}")

        # Заполнение первой строки матрицы A
        A[i][i - 1] = y_i_l
        A[i][i] = y_i
        A[i][i + 1] = y_i_r

        # Заполнение первой строки матрицы b
        b[i][0] = answer

    # Возвращаем измененные матрицы A и b
    return A, b


# Функция создания последнего краевого условия
def last_condition(A, b, x, h):
    # Вычисление коэффициентов для матрицы A
    y_4 = b_2()
    y_5 = -4 * b_2()
    y_6 = 2 * h * a_2() + 3 * b_2()

    # Вычисление коэффициента для матрицы b
    answer = 2 * h * c_2()

    # Вывод первого ограничения
    print(f"{6}: ({y_4:.4f})y4 + ({y_5:.4f})y5 + ({y_6:.4f})y6 = {answer:.4f}")

    # Заполнение первой строки матрицы A
    A[n][n - 2] = y_4
    A[n][n - 1] = y_5
    A[n][n] = y_6

    # Заполнение первой строки матрицы b
    b[n][0] = answer

    # Возвращаем измененные матрицы A и b
    return A, b


# Коэффициенты из условий
def p(x):
    return 2 / x


def q(x):
    return -3


def f(x):
    return 2


def a_1():
    return 0


def b_1():
    return 1


def c_1():
    return 1.5


def a_2():
    return 2


def b_2():
    return 1


def c_2():
    return 3


# Корректировка матрицы для метода прогонки
def matrix_adjustment(A, b, n):
    # Убираем лишний элемент из первой строки
    upper_factor = A[0][2] / A[1][2]
    A[0] -= A[1] * upper_factor
    b[0] -= b[1] * upper_factor

    print(">Убран третий элемент из первой строки")
    draw_matrix(A, b)

    # Убираем лишний коэффициент из последней строки
    down_factor = A[n][n - 2] / A[n - 1][n - 2]
    A[n] -= A[n - 1] * down_factor
    b[n] -= b[n - 1] * down_factor

    print(">Убран третий с конца элемент из последней строки")
    draw_matrix(A, b)

    return A, b


# Метод прогонки или метод Томаса
def solution_by_thomas_method(A, b):
    n = len(b)

    for i in range(1, n):
        m = A[i][i - 1] / A[i - 1][i - 1]
        A[i][i] -= m * A[i - 1][i]
        b[i][0] -= m * b[i - 1][0]

    x = np.zeros(n)
    x[n - 1] = b[n - 1][0] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (b[i][0] - A[i][i + 1] * x[i + 1]) / A[i][i]

    return x


# Вывод матриц
def draw_matrix(A, b):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{(A[i][j]):.4f}", end="  ")
        print(f"|  {(b[i][0]):.4f}", end="\n")


# Главный конструктор
def main_constructor(A, b, x, h, n):
    print("~~Создание уравнений и заполнение матрицы~~")
    A, b = first_condition(A, b, x, h)
    A, b = middle_conditions(A, b, x, h)
    A, b = last_condition(A, b, x, h)
    print()

    print("~~Вывод матриц~~")
    draw_matrix(A, b)
    print()

    print("~~Корректировка матрицы~~")
    A, b = matrix_adjustment(A, b, n)
    print()

    print("~~Решение методом прогонки~~")
    print(*solution_by_thomas_method(A, b), sep="\n")


# Интервал и шаг
x_0 = 0.8
x_n = 1.1
h = 0.05

# Количество уравнений n + 1
# 6
n = int((x_n - x_0 + 0.01) // h)

# Матрица x`ов
# 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1
x = [float("{:.2f}".format(i)) for i in np.arange(x_0, x_n, h)]
print(x)

# Заполнение матриц A(n + 1 X n + 1) и b(n + 1 X 1) нулями
A = np.zeros((n + 1, n + 1))
b = np.zeros((n + 1, 1))

# Вызов главного конструктора
main_constructor(A, b, x, h, n)
