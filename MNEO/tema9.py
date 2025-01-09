import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y + x

def exact_solution(x):
    return 2 * np.exp(x) - x - 1

def euler_method(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def heun_method(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y[i + 1] = y[i] + (h / 2) * (k1 + k2)
    return x, y

def runge_kutta_2(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
        y[i + 1] = y[i] + h * k2
    return x, y

def runge_kutta_3(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
        k3 = f(x[i] + h, y[i] - h * k1 + 2 * h * k2)
        y[i + 1] = y[i] + (h / 6) * (k1 + 4 * k2 + k3)
    return x, y

def runge_kutta_4(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    for i in range(n):
        k1 = f(x[-1], y[-1])
        k2 = f(x[-1] + h / 2, y[-1] + h * k1 / 2)
        k3 = f(x[-1] + h / 2, y[-1] + h * k2 / 2)
        k4 = f(x[-1] + h, y[-1] + h * k3)
        y_next = y[-1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x[-1] + h
        x.append(x_next)
        y.append(y_next)
    return np.array(x), np.array(y)

x0, y0 = 0, 1
h = 0.5
n = int(1 / h)

x_euler, y_euler = euler_method(f, x0, y0, h, n)
x_heun, y_heun = heun_method(f, x0, y0, h, n)
x_rk2, y_rk2 = runge_kutta_2(f, x0, y0, h, n)
x_rk3, y_rk3 = runge_kutta_3(f, x0, y0, h, n)
x_rk4, y_rk4 = runge_kutta_4(f, x0, y0, h, n)

x_exact = np.linspace(x0, x0 + n * h, n + 1)
y_exact = exact_solution(x_exact)

print("Erorile la x final:")
print(f"Euler: {abs(y_euler[-1] - y_exact[-1])}")
print(f"Heun: {abs(y_heun[-1] - y_exact[-1])}")
print(f"Runge-Kutta Ord. 2: {abs(y_rk2[-1] - y_exact[-1])}")
print(f"Runge-Kutta Ord. 3: {abs(y_rk3[-1] - y_exact[-1])}")
print(f"Runge-Kutta Ord. 4: {abs(y_rk4[-1] - y_exact[-1])}")

plt.figure(figsize=(10, 6))
plt.plot(x_exact, y_exact, 'k-', label="Soluția exactă")
plt.plot(x_euler, y_euler, 'g-', label="Metoda Euler")
plt.plot(x_heun, y_heun, 'r-.', label="Metoda Heun")
plt.plot(x_rk2, y_rk2, 'b:', label="Runge-Kutta Ord. 2")
plt.plot(x_rk3, y_rk3, 'm-', label="Runge-Kutta Ord. 3")
plt.plot(x_rk4, y_rk4, 'c-', label="Runge-Kutta Ord. 4")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Compararea metodelor numerice la h = 0.5")
plt.legend()
plt.grid()
plt.show()
