import numpy as np

# *** Metoda Gauss-Seidel pentru primul sistem ***

# Funcțiile F(x, y) și G(x, y) pentru primul sistem
def F(y):
    return np.sqrt(5 - y**2)

def G(x):
    return 2 / x

# Algoritmul Gauss-Seidel pentru primul sistem
def gauss_seidel_nonlinear(tol=1e-4, max_iter=100):
    x, y = 1.5, 1.5  # Punctul inițial

    for i in range(max_iter):
        x_next = F(y)
        y_next = G(x_next)

        if abs(x_next - x) < tol and abs(y_next - y) < tol:
            return x_next, y_next, i + 1  # Soluția și numărul de iterații

        x, y = x_next, y_next

    return None

# *** Metoda Gauss-Seidel pentru al doilea sistem ***

# Funcțiile de recurență definite conform enunțului
def compute_x_next(y, z, x):
    return np.sqrt(0.5 * (y * z + 5 * x - 1))

def compute_y_next(x_next, z):
    return np.sqrt(2 * x_next + np.log(z))

def compute_z_next(x_next, y_next, z):
    return np.sqrt(x_next * y_next + 2 * z + 8)

# Algoritmul Gauss-Seidel pentru al doilea sistem
def gauss_seidel_system2(tol=0.001, max_iter=100):
    x, y, z = 10.0, 10.0, 10.0  # Punctul inițial

    for _ in range(max_iter):
        x_next = compute_x_next(y, z, x)
        y_next = compute_y_next(x_next, z)
        z_next = compute_z_next(x_next, y_next, z)

        if (
            abs(x_next - x) < tol and
            abs(y_next - y) < tol and
            abs(z_next - z) < tol
        ):
            return x_next, y_next, z_next

        x, y, z = x_next, y_next, z_next

    return None

# *** Metoda Newton-Raphson pentru al treilea sistem ***

# Funcțiile f și g
def f(x, y):
    return 2 * x**2 - x * y - 5 * x + 1

def g(x, y):
    return x + 3 * np.log10(x) - y**2

# Derivatele parțiale
def dfdx(x, y):
    return 4 * x - y - 5

def dfdy(x, y):
    return -x

def dgdx(x, y):
    return 1 + 3 / (x * np.log(10))

def dgdy(x, y):
    return -2 * y

# Algoritmul Newton-Raphson
def safe_newton_raphson_system(x0, y0, tol=1e-6, max_iter=100):
    x, y = x0, y0
    for _ in range(max_iter):
        if x <= 0:
            return None

        F = np.array([f(x, y), g(x, y)])
        J = np.array([
            [dfdx(x, y), dfdy(x, y)],
            [dgdx(x, y), dgdy(x, y)]
        ])

        delta = np.linalg.solve(J, -F)
        x, y = x + delta[0], y + delta[1]

        if np.linalg.norm(delta) < tol:
            return x, y

    return None

# *** Apeluri și afișări ***

# 1. Gauss-Seidel pentru primul sistem
solution1 = gauss_seidel_nonlinear()
if solution1:
    print(f"Soluția sistemului (primul Gauss-Seidel): x = {solution1[0]:.6f}, y = {solution1[1]:.6f}, iterații = {solution1[2]}")
else:
    print("Primul sistem nu a convergent.")

# 2. Gauss-Seidel pentru al doilea sistem
solution2 = gauss_seidel_system2()
if solution2:
    print(f"Soluția sistemului (al doilea Gauss-Seidel): x = {solution2[0]:.6f}, y = {solution2[1]:.6f}, z = {solution2[2]:.6f}")
else:
    print("Al doilea sistem nu a convergent.")

# 3. Newton-Raphson pentru al treilea sistem
initial_points = [(0.5, 0.5), (2, 2), (1.5, 1.5), (0.8, 0.8)]
print("Rezultatele metodei Newton-Raphson:")
for x0, y0 in initial_points:
    solution3 = safe_newton_raphson_system(x0, y0)
    print(f"Punct inițial: ({x0}, {y0}), Soluție: {solution3}")


