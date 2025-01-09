import numpy as np
import matplotlib.pyplot as plt

def exact_solution_1(x):
    return x**2 - 2*x + 2 - np.exp(-x)

def f1(x, y):
    return x**2 - y

def exact_solution_2(x):
    return 2 * np.exp(x) - x - 1

def f2(x, y):
    return y + x

def euler_method_1(h):
    x_values = np.arange(0, 4 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_values.append(y_values[-1] + h * f1(x_values[i - 1], y_values[-1]))
    return x_values, y_values

def euler_method_2(h):
    x_values = np.arange(0, 1 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_values.append(y_values[-1] + h * f2(x_values[i - 1], y_values[-1]))
    return x_values, y_values

def modified_euler_method_1(h):
    x_values = np.arange(0, 4 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f1(x_values[i - 1], y_values[-1])
        y_values.append(y_values[-1] + h * 0.5 * (f1(x_values[i - 1], y_values[-1]) + f1(x_values[i], y_predict)))
    return x_values, y_values

def modified_euler_method_2(h):
    x_values = np.arange(0, 1 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f2(x_values[i - 1], y_values[-1])
        y_values.append(y_values[-1] + h * 0.5 * (f2(x_values[i - 1], y_values[-1]) + f2(x_values[i], y_predict)))
    return x_values, y_values

def euler_heun_method_1(h):
    x_values = np.arange(0, 4 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f1(x_values[i - 1], y_values[-1]) 
        y_values.append(y_values[-1] + h * 0.5 * (f1(x_values[i - 1], y_values[-1]) + f1(x_values[i], y_predict)))
    return x_values, y_values

def euler_heun_method_2(h):
    x_values = np.arange(0, 1 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f2(x_values[i - 1], y_values[-1])
        y_values.append(y_values[-1] + h * 0.5 * (f2(x_values[i - 1], y_values[-1]) + f2(x_values[i], y_predict))) 
    return x_values, y_values

h = 0.5
x_euler_1, y_euler_1 = euler_method_1(h)
x_mod_euler_1, y_mod_euler_1 = modified_euler_method_1(h)
x_euler_heun_1, y_euler_heun_1 = euler_heun_method_1(h)

x_euler_2, y_euler_2 = euler_method_2(h)
x_mod_euler_2, y_mod_euler_2 = modified_euler_method_2(h)
x_euler_heun_2, y_euler_heun_2 = euler_heun_method_2(h)

y_exact_1 = exact_solution_1(x_euler_1)
y_exact_mod_euler_1 = exact_solution_1(x_mod_euler_1)
y_exact_euler_heun_1 = exact_solution_1(x_euler_heun_1)

y_exact_2 = exact_solution_2(x_euler_2)
y_exact_mod_euler_2 = exact_solution_2(x_mod_euler_2)
y_exact_euler_heun_2 = exact_solution_2(x_euler_heun_2)

error_euler_1 = np.abs(y_exact_1 - y_euler_1)
error_mod_euler_1 = np.abs(y_exact_mod_euler_1 - y_mod_euler_1)
error_euler_heun_1 = np.abs(y_exact_euler_heun_1 - y_euler_heun_1)

error_euler_2 = np.abs(y_exact_2 - y_euler_2)
error_mod_euler_2 = np.abs(y_exact_mod_euler_2 - y_mod_euler_2)
error_euler_heun_2 = np.abs(y_exact_euler_heun_2 - y_euler_heun_2)

print("Rezultate pentru Problema 1 (h = 0.5):")
print("Metoda Euler - erori:", error_euler_1)
print("Metoda Modificată a lui Euler - erori:", error_mod_euler_1)
print("Metoda Euler-Heun - erori:", error_euler_heun_1)

print("Rezultate pentru Problema 2 (h = 0.5):")
print("Metoda Euler - erori:", error_euler_2)
print("Metoda Modificată a lui Euler - erori:", error_mod_euler_2)
print("Metoda Euler-Heun - erori:", error_euler_heun_2)

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(x_euler_1, y_euler_1, label='Euler Method', marker='o')
plt.plot(x_euler_1, y_exact_1, label='Exact Solution', linestyle='dashed')
plt.plot(x_mod_euler_1, y_mod_euler_1, label='Modified Euler Method', marker='x')
plt.plot(x_euler_heun_1, y_euler_heun_1, label='Euler-Heun Method', marker='s')
plt.title('Problema 1: Comparam metodele')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x_euler_2, y_euler_2, label='Euler Method', marker='o')
plt.plot(x_euler_2, y_exact_2, label='Exact Solution', linestyle='dashed')
plt.plot(x_mod_euler_2, y_mod_euler_2, label='Modified Euler Method', marker='x')
plt.plot(x_euler_heun_2, y_euler_heun_2, label='Euler-Heun Method', marker='s')
plt.title('Problema 2: Comparam metodele')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
