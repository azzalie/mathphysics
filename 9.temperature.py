import numpy as np


def f(x):
    return np.sin(x + 0.45)


def phi(t):
    return 0.435 - 2 * t


def psi(t):
    return 0.8674


def initial_temperature(x, h_x, n1, u):
    for i in range(n1 + 1):
        u[0][i] = f(x)
        x += h_x

    return u


def boundary_conditions(t, h_t, n1, n2, u):
    for j in range(n2 + 1):
        u[j][0] = phi(t)
        u[j][n1] = psi(t)
        t += h_t

    return u


def completion(u, n1, n2, h_x, h_t):
    for i in range(1, n2 + 1):
        for j in range(1, n1):
            u[i][j] = u[i - 1][j] * (1 - (2 * h_t) / (h_x ** 2)) + (
                    h_t / (h_x ** 2)
            ) * (u[i - 1][j + 1] + u[i - 1][j - 1])

        print("Итерация", i)
        print_res(u)

    return u


def conductivity(x, t, x_final, t_final, h_x, h_t):
    n1 = round((x_final - x) / h_x)
    n2 = round((t_final - t) / h_t)

    u = np.zeros((n1 + 1, n2 + 1))

    u = initial_temperature(x, h_x, n1, u)
    print("Начальная температура")
    print_res(u)

    u = boundary_conditions(t, h_t, n1, n2, u)
    print("Краевые условия")
    print_res(u)

    print("Заполнение матрицы")
    u = completion(u, n1, n2, h_x, h_t)

    print("Ответ")
    print_res(u)

    return u


def print_res(arr):
    for i in arr:
        for j in i:
            print(f"{j:.4f}", end="\t|\t")
        print()
    print()


x = 0
t = 0

x_final = 0.6
t_final = 0.01

h_x = 0.1
h_t = 0.0017

conductivity(x, t, x_final, t_final, h_x, h_t)
