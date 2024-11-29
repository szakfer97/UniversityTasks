import numpy as np

# Definirea funcțiilor și derivatelor lor
def f1(x):
    return x**2 - 2

def df1(x):
    return 2 * x

def f2(x):
    return x**3 - x - 1

def df2(x):
    return 3 * x**2 - 1

# Metoda de ordinul 3 pentru aproximarea rădăcinii pătrate
def method_order_3(a, eps):
    x = a  # Initial guess
    iterations = 0
    while True:
        next_x = x * (abs(x**2) + 3 * a) / (3 * abs(x**2) + a) 
        iterations += 1
        if abs(next_x - x) < eps:
            break
        x = next_x
    return x, iterations

# Metoda combinată a tangentei (hibridă între Newton-Raphson și bisection)
def combined_tangent_method(f, df, a, b, x0, eps):
    x = x0
    iterations = 0
    while abs(f(x)) > eps:
        iterations += 1
        if x < a or x > b:  
            x = (a + b) / 2
        else:  # Metoda tangentei
            x = x - f(x) / df(x)
        
        # Updatam intervalul [a, b]
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return x, iterations

# Metoda tangentei (Newton-Raphson)
def tangent_method(f, df, x0, eps):
    x = x0
    iterations = 0
    while abs(f(x)) > eps:
        iterations += 1
        x = x - f(x) / df(x)
    return x, iterations

# Parametri
a1, b1 = 1, 2  # Interval pentru f1
a2, b2 = 1, 2  # Interval pentru f2
x0 = 2
eps_values = [10**-4, 10**-8, 10**-12]

# Afișarea rezultatelor pentru sqrt(2) folosind metoda de ordinul 3
a_sqrt2 = 2
results_order_3_sqrt2 = [method_order_3(a_sqrt2, eps) for eps in eps_values]

# Afișarea rezultatelor pentru sqrt(5) folosind metoda de ordinul 3
a_sqrt5 = 5
results_order_3_sqrt5 = [method_order_3(a_sqrt5, eps) for eps in eps_values]

# Calcularea rezultatelor pentru f1 (x^2 - 2) folosind metodele combinate și tangentei
results_combined_f1 = [combined_tangent_method(f1, df1, a1, b1, x0, eps) for eps in eps_values]
results_tangent_f1 = [tangent_method(f1, df1, x0, eps) for eps in eps_values]

# Calcularea rezultatelor pentru f2 (x^3 - x - 1) folosind metodele combinate și tangentei
results_combined_f2 = [combined_tangent_method(f2, df2, a2, b2, x0, eps) for eps in eps_values]
results_tangent_f2 = [tangent_method(f2, df2, x0, eps) for eps in eps_values]

# Afișarea rezultatelor pentru sqrt(2) folosind metoda de ordinul 3
print("Aproximări pentru sqrt(2):")
print("Metoda de ordinul 3:")
for eps, (approx, iters) in zip(eps_values, results_order_3_sqrt2):
    print(f"Epsilon: {eps}, Aproximare: {approx}, Iterații: {iters}")

# Afișarea rezultatelor pentru sqrt(5) folosind metoda de ordinul 3
print("\nAproximări pentru sqrt(5):")
print("Metoda de ordinul 3:")
for eps, (approx, iters) in zip(eps_values, results_order_3_sqrt5):
    print(f"Epsilon: {eps}, Aproximare: {approx}, Iterații: {iters}")

# Afișarea rezultatelor pentru f1(x)
print("\nRezultate pentru f(x) = x^2 - 2:")
print("Metoda combinată a tangentei:")
for eps, (approx, iters) in zip(eps_values, results_combined_f1):
    print(f"Epsilon: {eps}, Aproximare: {approx}, Iterații: {iters}")

print("\nMetoda tangentei:")
for eps, (approx, iters) in zip(eps_values, results_tangent_f1):
    print(f"Epsilon: {eps}, Aproximare: {approx}, Iterații: {iters}")

# Afișarea rezultatelor pentru f2(x)
print("\nRezultate pentru f(x) = x^3 - x - 1:")
print("Metoda combinată a tangentei:")
for eps, (approx, iters) in zip(eps_values, results_combined_f2):
    print(f"Epsilon: {eps}, Aproximare: {approx}, Iterații: {iters}")

print("\nMetoda tangentei:")
for eps, (approx, iters) in zip(eps_values, results_tangent_f2):
    print(f"Epsilon: {eps}, Aproximare: {approx}, Iterații: {iters}")