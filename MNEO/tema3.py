import math

def f(x):
    return x**2 - 2

def df(x):
    return 2 * x

def ddf(x):
    return 2

def halley_method(x0, epsilon):
    iterations = 0
    while abs(f(x0)) > epsilon:
        numerator = 2 * f(x0) * df(x0)
        denominator = 2 * (df(x0)**2) - f(x0) * ddf(x0)
        x0 = x0 - numerator / denominator
        iterations += 1
    return x0, iterations

def newton_method(x0, epsilon):
    iterations = 0
    while abs(f(x0)) > epsilon:
        x0 = x0 - f(x0) / df(x0)
        iterations += 1
    return x0, iterations

epsilons = [10**-4, 10**-8, 10**-12]
x0_halley = 2 
x0_newton = 2  
results = []

for eps in epsilons:
    root_halley, iter_halley = halley_method(x0_halley, eps)
    error_halley = abs(math.sqrt(2) - root_halley)
    
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
