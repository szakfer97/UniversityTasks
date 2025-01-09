import math

def f_sqrt2(x):
    return x**2 - 2

def df_sqrt2(x):
    return 2 * x

def f_cubic(x):
    return x**3 - x - 1

def df_cubic(x):
    return 3 * x**2 - 1

def secant_method(x0, x1, epsilon, func):
    iterations = 0
    while abs(func(x1)) > epsilon:
        try:
            x_next = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        except ZeroDivisionError:
            break
        x0, x1 = x1, x_next
        iterations += 1
    return x1, iterations

def newton_method(x0, epsilon, func, dfunc):
    iterations = 0
    while abs(func(x0)) > epsilon:
        x0 = x0 - func(x0) / dfunc(x0)
        iterations += 1
    return x0, iterations

epsilons = [10**-4, 10**-8, 10**-12]

def display_results(title, results):
    print(title)
    for result in results:
        print(f"Epsilon: {result['epsilon']}")
        print(f"  Metoda secantei:")
        print(f"    Rădăcina: {result['secant_root']}")
        print(f"    Iterații: {result['secant_iterations']}")
        print(f"    Eroare: {result['secant_error']}")
        print(f"  Metoda tangentei:")
        print(f"    Rădăcina: {result['newton_root']}")
        print(f"    Iterații: {result['newton_iterations']}")
        print(f"    Eroare: {result['newton_error']}")
        print()

x0_secant, x1_secant = 2, 1.4
x0_newton = 2
results_sqrt2 = []

for eps in epsilons:
    root_secant, iter_secant = secant_method(x0_secant, x1_secant, eps, f_sqrt2)
    error_secant = abs(math.sqrt(2) - root_secant)
    
    root_newton, iter_newton = newton_method(x0_newton, eps, f_sqrt2, df_sqrt2)
    error_newton = abs(math.sqrt(2) - root_newton)
    
    results_sqrt2.append({
        "epsilon": eps,
        "secant_root": root_secant,
        "secant_iterations": iter_secant,
        "secant_error": error_secant,
        "newton_root": root_newton,
        "newton_iterations": iter_newton,
        "newton_error": error_newton
    })

x0_secant_cubic, x1_secant_cubic = 2, 1.5
x0_newton_cubic = 2
results_cubic = []

for eps in epsilons:
    root_secant_cubic, iter_secant_cubic = secant_method(x0_secant_cubic, x1_secant_cubic, eps, f_cubic)
    error_secant_cubic = abs(root_secant_cubic - 1.324717957244746)  # Valoarea exactă
    
    root_newton_cubic, iter_newton_cubic = newton_method(x0_newton_cubic, eps, f_cubic, df_cubic)
    error_newton_cubic = abs(root_newton_cubic - 1.324717957244746)  # Valoarea exactă
    
    results_cubic.append({
        "epsilon": eps,
        "secant_root": root_secant_cubic,
        "secant_iterations": iter_secant_cubic,
        "secant_error": error_secant_cubic,
        "newton_root": root_newton_cubic,
        "newton_iterations": iter_newton_cubic,
        "newton_error": error_newton_cubic
    })

display_results("Rezultate pentru funcția f(x) = x^2 - 2:", results_sqrt2)
display_results("Rezultate pentru funcția f(x) = x^3 - x - 1:", results_cubic)
