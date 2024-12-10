import numpy as np
import matplotlib.pyplot as plt

# Definirea ecuației diferențiale și a soluției exacte
def f(x, y):
    return y + x

def exact_solution(x):
    return 2 * np.exp(x) - x - 1

# Metoda Euler
def euler_method(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

# Metoda Heun
def heun_method(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y[i + 1] = y[i] + (h / 2) * (k1 + k2)
    return x, y

# Metoda Runge-Kutta de ordinul 2
def runge_kutta_2(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
        y[i + 1] = y[i] + h * k2
    return x, y

# Metoda Runge-Kutta de ordinul 3
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

# Setările problemei
x0, y0 = 0, 1
h = 0.5
n = int(1 / h)

# Calculul soluțiilor
x_euler, y_euler = euler_method(f, x0, y0, h, n)
x_heun, y_heun = heun_method(f, x0, y0, h, n)
x_rk2, y_rk2 = runge_kutta_2(f, x0, y0, h, n)
x_rk3, y_rk3 = runge_kutta_3(f, x0, y0, h, n)

# Soluția exactă
x_exact = np.linspace(x0, x0 + n * h, n + 1)
y_exact = exact_solution(x_exact)

# Calculul erorilor
print("Erorile la x final:")
print(f"Euler: {abs(y_euler[-1] - y_exact[-1])}")
print(f"Heun: {abs(y_heun[-1] - y_exact[-1])}")
print(f"Runge-Kutta Ord. 2: {abs(y_rk2[-1] - y_exact[-1])}")
print(f"Runge-Kutta Ord. 3: {abs(y_rk3[-1] - y_exact[-1])}")

# Afișarea rezultatelor
plt.figure(figsize=(10, 6))
plt.plot(x_exact, y_exact, 'k-', label="Soluția exactă")
plt.plot(x_euler, y_euler, 'r--', label="Metoda Euler")
plt.plot(x_heun, y_heun, 'g-.', label="Metoda Heun")
plt.plot(x_rk2, y_rk2, 'b:', label="Runge-Kutta Ord. 2")
plt.plot(x_rk3, y_rk3, 'm-', label="Runge-Kutta Ord. 3")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Compararea metodelor numerice la h = 0.5")
plt.legend()
plt.grid()
plt.show()
