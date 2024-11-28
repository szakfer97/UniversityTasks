import math

def metoda_newton(f, df, x0, eps):
    """
    Metodă generică Newton pentru găsirea rădăcinilor
    
    Parametri:
    f: funcția pentru care căutăm rădăcina
    df: derivata funcției
    x0: punct inițial
    eps: precizie dorită
    
    Returnează:
    n: număr de iterații
    x: rădăcina aproximată
    """
    x = [x0]
    n = 0
    
    while True:
        x_nou = x[n] - f(x[n]) / df(x[n])
        x.append(x_nou)
        
        if abs(x[n+1] - x[n]) <= eps:
            return n+1, x[n+1]
        
        n += 1

# Exemplul 1: x^3 - x - 1 = 0
def f1(x):
    return x**3 - x - 1

def df1(x):
    return 3*x**2 - 1

# Exemplul 2: x^5 - 5x + 1 = 0
def f2(x):
    return x**5 - 5*x + 1

def df2(x):
    return 5*x**4 - 5

# Exemplul 3: Ecuația lui Kepler
def f3(x):
    return x - math.sin(x) - 0.25

def df3(x):
    return 1 - math.cos(x)

# Calculul radicalilor
def radical_tangenta(k, c, eps):
    """
    Calculează radicalul de ordin k din c folosind metoda tangentei.
    """
    # Alegerea x0
    x0 = c if c > 1 else 1
    
    def f(x):
        return x**k - c

    def df(x):
        return k * x**(k-1)
    
    iteratii, radacina = metoda_newton(f, df, x0, eps)
    return iteratii, radacina

# Testare pentru radicali
def test_radicali():
    precizii = [10**-4, 10**-8, 10**-12]
    valori = [
        (2, 2),  # sqrt(2)
        (2, 3),  # sqrt(3)
        (2, 5),  # sqrt(5)
        (3, 2),  # cuberoot(2)
        (3, 3),  # cuberoot(3)
        (3, 1/2) # cuberoot(1/2)
    ]

    for k, c in valori:
        print(f"\nRadical de ordin {k} din {c}:")
        for eps in precizii:
            iteratii, radacina = radical_tangenta(k, c, eps)
            print(f"ε = {eps}: Iterații = {iteratii}, Rădăcină = {radacina:.12f}")

# Testare exemple din fișier
precizii = [10**-4, 10**-8, 10**-12]

print("Exemplul 1: x^3 - x - 1 = 0")
for eps in precizii:
    iteratii, radacina = metoda_newton(f1, df1, 1.5, eps)
    print(f"ε = {eps}: Iterații = {iteratii}, Rădăcină = {radacina:.12f}")

print("\nExemplul 2: x^5 - 5x + 1 = 0")
for eps in precizii:
    iteratii, radacina = metoda_newton(f2, df2, 0, eps)
    print(f"ε = {eps}: Iterații = {iteratii}, Rădăcină = {radacina:.12f}")

print("\nExemplul 3: Ecuația lui Kepler (x = sin(x) + 0.25)")
x0 = 3 * math.pi / 8  # ≈ 1.1781, valoarea inițială dată
eps = 10**-4
iteratii, radacina = metoda_newton(f3, df3, x0, eps)
print(f"ε = {eps}: Iterații = {iteratii}, Rădăcină = {radacina:.12f}")

# Testare radicali
print("\nCalculul radicalilor cu metoda tangentei:")
test_radicali()
