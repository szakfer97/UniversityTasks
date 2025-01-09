import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (1 / (1 + x**2)) - 2 * y**2

def exact_solution(x):
    return x / (1 + x**2)

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

x0 = 0
y0 = 0
h = 1 / 4
n = 16
x_rk4, y_rk4 = runge_kutta_4(f, x0, y0, h, n)

x_exact = np.linspace(x0, x0 + n * h, 1000)
y_exact = exact_solution(x_exact)

y_exact_points = exact_solution(x_rk4)
errors = np.abs(y_rk4 - y_exact_points)

print("Erorile la punctele considerate:")
for i in range(len(x_rk4)):
    print(f"x = {x_rk4[i]:.2f}, y_RK4 = {y_rk4[i]:.6f}, y_exact = {y_exact_points[i]:.6f}, eroare = {errors[i]:.6e}")

plt.figure(figsize=(10, 6))
plt.plot(x_exact, y_exact, 'k-', label="Soluția exactă")
plt.plot(x_rk4, y_rk4, 'r--o', label="Runge-Kutta Ord. 4 (RK4)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Compararea soluției exacte cu metoda Runge-Kutta 4")
plt.legend()
plt.grid()

plt.figure(figsize=(10, 6))
plt.plot(x_rk4, errors, 'b-o', label="Eroarea absolută |y_exact - y_rk4|")
plt.xlabel("x")
plt.ylabel("Eroare absolută")
plt.title("Eroarea absolută în funcție de x")
plt.legend()
plt.grid()
plt.show()
