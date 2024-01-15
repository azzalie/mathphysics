import matplotlib.pyplot as plt
import numpy as np


def temp_runge_kutty(x0, y0, h):
    print(f"h = {h}, x = {x0}, y = {y0}")
    k1 = f(x0, y0)
    k2 = f(x0 + h / 2, y0 + h / 2 * k1)
    k3 = f(x0 + h / 2, y0 + h / 2 * k2)
    k4 = f(x0 + h, y0 + h * k3)

    y0 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    print(
        f"k1 = {k1:.6f}\n"
        f"k2 = {k2:.6f}\n"
        f"k3 = {k3:.6f}\n"
        f"k4 = {k4:.6f}\n"
        f"--> y = {y0:.6f}"
    )

    return y0


def refine_step(x0, y0, a, b, h, e):
    print("Вычисление уточненного шага")
    step = 0
    i = 1
    t = h
    while step <= e:
        print(f"Итерация: {i}")
        y1 = temp_runge_kutty(x0, y0, t)
        y2 = temp_runge_kutty(x0 + t, y1, t)
        y1_2 = temp_runge_kutty(x0, y0, 2 * t)
        y2_2 = temp_runge_kutty(x0 + 2 * t, y1_2, 2 * t)
        step = np.abs(y2 - y1_2)

        print(
            f"y1 = {y1:.6f}\n"
            f"y2 = {y2:.6f}\n"
            f"y1~ = {y1_2:.6f}\n"
            f"y2~ = {y2_2:.6f}\n"
            f"Шаг: {h}\n"
            f"Погрешность: y2 - y2~ = {y2:.6f} - {y2_2:.6f} = {step:.6f}\n"
        )
        t += h
        i += 1

    h = t - h

    n = (b - a) / h
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    print(f"n = {n}\n" f"h = {h}\n" f"Конецъ\n")
    return h


def runge_kutty(x0, y0, b, h):
    classic_x = [x0]
    classic_y = [y0]

    while x0 < b:
        k1 = f(x0, y0)
        k2 = f(x0 + h / 2, y0 + h / 2 * k1)
        k3 = f(x0 + h / 2, y0 + h / 2 * k2)
        k4 = f(x0 + h, y0 + h * k3)

        y0 += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h

        classic_x.append(x0)
        classic_y.append(y0)

    return classic_x, classic_y


def classic_euler(x0, y0, b, h):
    x_values = [x0]
    y_values = [y0]

    while x0 <= b:
        y0 += h * f(x0, y0)
        x0 += h

        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values


def f(x, y):
    return (12 * y - (5 * (x ** 2) + 3) * (y ** 3)) / (8 * x)


def points(x_single, y_single, x_double, y_double):
    new_y_double = []
    j = 0
    for i in range(len(y_single)):
        if i % 2 == 0:
            new_y_double.append(y_double[j])
            j += 1
        else:
            new_y_double.append("")
    print("x", " " * 4, "y(h)", " " * 4, "y(2h)", " " * 3, "Погрешность:")
    delta = []
    for i in range(len(y_single)):
        if new_y_double[i] != "":
            if abs(y_single[i] - new_y_double[i]):
                delta.append(abs(y_single[i] - new_y_double[i]))
            print(
                f"{x_single[i]:.1f}{' ' * 4}"
                f"{y_single[i]:.6f}{' ' * 2}"
                f"{new_y_double[i]:.6f}{' ' * 2}"
                f"{abs(y_single[i] - new_y_double[i]):.9f}"
            )
        else:
            print(f"{x_single[i]:.1f}{' ' * 4}{y_single[i]:.6f}")
    print(f"Max и Min погрешность кроме 0\n{max(delta):.9f}{' ' * 4}{min(delta):.9f}")


x0 = 1
y0 = 1
a = 1
b = 3
e = 10 ** (-4)
h_single = e ** (1 / 4)
h_improv = refine_step(x0, y0, a, b, h_single, e)
# h_double = 2 * h_single

h_single = h_improv
h_double = h_single * 2

rk_x_single, rk_y_single = runge_kutty(x0, y0, b, h_single)
rk_x_double, rk_y_double = runge_kutty(x0, y0, b, h_double)
classic_x_single, classic_y_single = classic_euler(x0, y0, b, h_single)
classic_x_double, classic_y_double = classic_euler(x0, y0, b, h_double)

print("Метод Рунге-Кутты")
points(rk_x_single, rk_y_single, rk_x_double, rk_y_double)
print()
print("Метод Эйлера")
points(classic_x_single, classic_y_single, classic_x_double, classic_y_double)

plt.figure(figsize=(16, 9))
plt.plot(
    rk_x_single,
    rk_y_single,
    label="Метод Рунге-Кутты с обычным шагом",
)
plt.plot(
    rk_x_double,
    rk_y_double,
    label="Метод Рунге-Кутты с обычным шагом",
)
plt.plot(
    classic_x_single,
    classic_y_single,
    label="Метод Эйлера с обычным шагом",
)
plt.plot(
    classic_x_double,
    classic_y_double,
    label="Метод Эйлера с двойным шагом",
)
plt.legend()
plt.show()
