import numpy as np


def deflection(x, h, n, m, u):
    for i in range(n + 1):
        u[m][i] = f(x)
        if i != n + 1 and i != 0:
            u[m - 1][i] = phi_big(x) * h + f(x)
        x += h

    return u


def beginning(t, h, n, m, u):
    for i in range(m, -1, -1):
        u[i][0] = phi(t)
        u[i][n] = psi(t)
        t += h

    return u


def completion(n, m, u):
    for i in range(m - 1, 0, -1):
        for j in range(1, n):
            u[i - 1][j] = (
                    2 * (1 - ((h ** 2) / (h ** 2))) * u[i][j]
                    + ((h ** 2) / (h ** 2)) * (u[i][j + 1] + u[i][j - 1])
                    - u[i + 1][j]
            )

    return u


def f(x):
    return (x ** 2 + 1) * 0.5


def phi_big(x):
    return x * np.sin(2 * x)


def phi(t):
    return 0.5 + 3 * t


def psi(t):
    return 1


def assembly(x0, xn, t0, tn, h):
    n = round((xn - x0) / h)
    m = round((tn - t0) / h)

    u = np.zeros((m + 1, n + 1))
    u = deflection(x0, h, n, m, u)
    u = beginning(t0, h, n, m, u)
    u = completion(n, m, u)

    return u


x0, xn = 0, 1
t0, tn = 0, 0.5
h = 0.1

u = assembly(x0, xn, t0, tn, h)

for i in u[::-1]:
    for j in i:
        print(f"{j:.3f}", end=" ")
    print()
