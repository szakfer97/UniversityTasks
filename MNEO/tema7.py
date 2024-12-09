import numpy as np

# Soluția exactă și funcția pentru prima problemă
def exact_solution_1(x):
    return x**2 - 2*x + 2 - np.exp(-x)

def f1(x, y):
    return x**2 - y

# Soluția exactă și funcția pentru a doua problemă
def exact_solution_2(x):
    return 2 * np.exp(x) - x - 1

def f2(x, y):
    return y + x

# Metoda lui Euler pentru prima problemă
def euler_method_1(h):
    x_values = np.arange(0, 4 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_values.append(y_values[-1] + h * f1(x_values[i - 1], y_values[-1]))
    return x_values, y_values

# Metoda lui Euler pentru a doua problemă
def euler_method_2(h):
    x_values = np.arange(0, 1 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_values.append(y_values[-1] + h * f2(x_values[i - 1], y_values[-1]))
    return x_values, y_values

# Metoda modificată a lui Euler (Heun) pentru prima problemă
def modified_euler_method_1(h):
    x_values = np.arange(0, 4 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f1(x_values[i - 1], y_values[-1])  # Predicția folosind Euler
        y_values.append(y_values[-1] + h * 0.5 * (f1(x_values[i - 1], y_values[-1]) + f1(x_values[i], y_predict)))  # Corectarea
    return x_values, y_values

# Metoda modificată a lui Euler (Heun) pentru a doua problemă
def modified_euler_method_2(h):
    x_values = np.arange(0, 1 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f2(x_values[i - 1], y_values[-1])  # Predicția folosind Euler
        y_values.append(y_values[-1] + h * 0.5 * (f2(x_values[i - 1], y_values[-1]) + f2(x_values[i], y_predict)))  # Corectarea
    return x_values, y_values

# Metoda Euler-Heun pentru prima problemă
def euler_heun_method_1(h):
    x_values = np.arange(0, 4 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f1(x_values[i - 1], y_values[-1])  # Predicția folosind Euler
        y_values.append(y_values[-1] + h * 0.5 * (f1(x_values[i - 1], y_values[-1]) + f1(x_values[i], y_predict)))  # Corectarea
    return x_values, y_values

# Metoda Euler-Heun pentru a doua problemă
def euler_heun_method_2(h):
    x_values = np.arange(0, 1 + h, h)
    y_values = [1]
    for i in range(1, len(x_values)):
        y_predict = y_values[-1] + h * f2(x_values[i - 1], y_values[-1])  # Predicția folosind Euler
        y_values.append(y_values[-1] + h * 0.5 * (f2(x_values[i - 1], y_values[-1]) + f2(x_values[i], y_predict)))  # Corectarea
    return x_values, y_values

# Calcul pentru h = 0.1
h = 0.1

# Aplicarea metodelor pentru problema 1
x_euler_1, y_euler_1 = euler_method_1(h)
x_mod_euler_1, y_mod_euler_1 = modified_euler_method_1(h)
x_euler_heun_1, y_euler_heun_1 = euler_heun_method_1(h)

# Aplicarea metodelor pentru problema 2
x_euler_2, y_euler_2 = euler_method_2(h)
x_mod_euler_2, y_mod_euler_2 = modified_euler_method_2(h)
x_euler_heun_2, y_euler_heun_2 = euler_heun_method_2(h)

# Calcularea soluțiilor exacte pentru problema 1
y_exact_1 = exact_solution_1(x_euler_1)
y_exact_mod_euler_1 = exact_solution_1(x_mod_euler_1)
y_exact_euler_heun_1 = exact_solution_1(x_euler_heun_1)

# Calcularea soluțiilor exacte pentru problema 2
y_exact_2 = exact_solution_2(x_euler_2)
y_exact_mod_euler_2 = exact_solution_2(x_mod_euler_2)
y_exact_euler_heun_2 = exact_solution_2(x_euler_heun_2)

# Calcularea erorii pentru fiecare metodă în problema 1
error_euler_1 = np.abs(y_exact_1 - y_euler_1)
error_mod_euler_1 = np.abs(y_exact_mod_euler_1 - y_mod_euler_1)
error_euler_heun_1 = np.abs(y_exact_euler_heun_1 - y_euler_heun_1)

# Calcularea erorii pentru fiecare metodă în problema 2
error_euler_2 = np.abs(y_exact_2 - y_euler_2)
error_mod_euler_2 = np.abs(y_exact_mod_euler_2 - y_mod_euler_2)
error_euler_heun_2 = np.abs(y_exact_euler_heun_2 - y_euler_heun_2)

# Compararea rezultatelor pentru problema 1
print("Rezultate pentru Problema 1 (h = 0.1):")
print("\nMetoda Euler - valori aproximative:", y_euler_1)
print("Metoda Euler - soluții exacte:", y_exact_1)
print("Metoda Euler - erori:", error_euler_1)

print("\nMetoda Modificată a lui Euler - valori aproximative:", y_mod_euler_1)
print("Metoda Modificată a lui Euler - soluții exacte:", y_exact_mod_euler_1)
print("Metoda Modificată a lui Euler - erori:", error_mod_euler_1)

print("\nMetoda Euler-Heun - valori aproximative:", y_euler_heun_1)
print("Metoda Euler-Heun - soluții exacte:", y_exact_euler_heun_1)
print("Metoda Euler-Heun - erori:", error_euler_heun_1)

# Compararea rezultatelor pentru problema 2
print("\nRezultate pentru Problema 2 (h = 0.1):")
print("\nMetoda Euler - valori aproximative:", y_euler_2)
print("Metoda Euler - soluții exacte:", y_exact_2)
print("Metoda Euler - erori:", error_euler_2)

print("\nMetoda Modificată a lui Euler - valori aproximative:", y_mod_euler_2)
print("Metoda Modificată a lui Euler - soluții exacte:", y_exact_mod_euler_2)
print("Metoda Modificată a lui Euler - erori:", error_mod_euler_2)

print("\nMetoda Euler-Heun - valori aproximative:", y_euler_heun_2)
print("Metoda Euler-Heun - soluții exacte:", y_exact_euler_heun_2)
print("Metoda Euler-Heun - erori:", error_euler_heun_2)


