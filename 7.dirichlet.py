import numpy as np


def dirichlet(x, y, h, e):
    n = int(1 / h)
    u = np.zeros((n + 1, n + 1))
    u_new = np.zeros((n + 1, n + 1))

    for j in range(n + 1):
        u[n][j] = bc(x, y)
        u[0][j] = da(x, y)
        u[j][n] = cd(x, y)
        u[j][0] = ab(x, y)

        u_new[n][j] = bc(x, y)
        u_new[0][j] = da(x, y)
        u_new[j][n] = cd(x, y)
        u_new[j][0] = ab(x, y)

        x += h
        y += h

    print("Границы")
    print_res(u_new)

    for i in range(1, n):
        k = (u[i][n] - u[i][0]) / n
        for j in range(1, n):
            u[i][j] = u[i][0] + j * k

    iter = 1
    while True:
        eps = []
        for i in range(1, n):
            for j in range(1, n):
                u_new[i][j] = (1 / 4) * (
                        u_new[i - 1][j] + u[i + 1][j] + u_new[i][j - 1] + u[i][j + 1]
                )

        print("Итерация:", iter)
        print_res(u_new)

        for i in range(n + 1):
            for j in range(n + 1):
                eps.append(abs(u_new[i][j] - u[i][j]))
                u[i][j] = u_new[i][j]

        if max(eps) < e:
            break

        iter += 1

    return u_new


def ab(x, y):
    return 20 * np.cos(np.pi * y / 2)


def bc(x, y):
    return 30 * x * (1 - x)


def cd(x, y):
    return 30 * y * (1 - y ** 2)


def da(x, y):
    return 20 * (1 - x ** 2)


def print_res(arr):
    for i in arr:
        for j in i:
            print(f"{j:.4f}", end="\t|\t")
        print()
    print()


x, y = 0, 0
h = 0.2
e = 0.01

dirichlet(x, y, h, e)
