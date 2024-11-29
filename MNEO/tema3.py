import math

# Definirea funcției, derivatei și derivatei a doua
def f(x):
    return x**2 - 2

def df(x):
    return 2 * x

def ddf(x):
    return 2

# Metoda lui Halley
def halley_method(x0, epsilon):
    iterations = 0
    while abs(f(x0)) > epsilon:
        numerator = 2 * f(x0) * df(x0)
        denominator = 2 * (df(x0)**2) - f(x0) * ddf(x0)
        x0 = x0 - numerator / denominator
        iterations += 1
    return x0, iterations

# Metoda tangentei (Newton-Raphson)
def newton_method(x0, epsilon):
    iterations = 0
    while abs(f(x0)) > epsilon:
        x0 = x0 - f(x0) / df(x0)
        iterations += 1
    return x0, iterations

# Valorile pentru epsilon
epsilons = [10**-4, 10**-8, 10**-12]
x0_halley = 2  # Valoare inițială pentru metoda lui Halley
x0_newton = 2  # Valoare inițială pentru metoda tangentei

# Stocare rezultate
results = []

for eps in epsilons:
    # Metoda lui Halley
    root_halley, iter_halley = halley_method(x0_halley, eps)
    error_halley = abs(math.sqrt(2) - root_halley)
    
    # Metoda tangentei
    root_newton, iter_newton = newton_method(x0_newton, eps)
    error_newton = abs(math.sqrt(2) - root_newton)
    
    results.append({
        "epsilon": eps,
        "halley_root": root_halley,
        "halley_iterations": iter_halley,
        "halley_error": error_halley,
        "newton_root": root_newton,
        "newton_iterations": iter_newton,
        "newton_error": error_newton
    })

# Afișare rezultate
print("Rezultate pentru metoda lui Halley și metoda tangentei:")
for result in results:
    print(f"Epsilon: {result['epsilon']}")
    print(f"  Metoda lui Halley:")
    print(f"    Rădăcina: {result['halley_root']}")
    print(f"    Iterații: {result['halley_iterations']}")
    print(f"    Eroare: {result['halley_error']}")
    print(f"  Metoda tangentei:")
    print(f"    Rădăcina: {result['newton_root']}")
    print(f"    Iterații: {result['newton_iterations']}")
    print(f"    Eroare: {result['newton_error']}")
    print()
