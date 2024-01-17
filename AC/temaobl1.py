import numpy as np
from sympy import symbols, Matrix, solve

def calcul_valori_proprii_si_polinom_caracteristic(matrice):
    x = symbols('x')
    
    # Calculează polinomul caracteristic
    polinom_caracteristic = (Matrix(matrice) - x * np.eye(len(matrice))).det()
    
    # Găsește valorile proprii rezolvând polinomul caracteristic
    valorile_proprii = solve(polinom_caracteristic, x)
    
    return valorile_proprii, polinom_caracteristic

# Introducerea ordinului matricei
ordin_matrice = int(input("Introduceti ordinul matricei (2 sau 3): "))

# Introducerea valorilor matricei
valori_matrice = []
for i in range(ordin_matrice):
    rand = []
    for j in range(ordin_matrice):
        valoare = float(input(f"Introduceti valoarea pentru matrice[{i+1}][{j+1}]: "))
        rand.append(valoare)
    valori_matrice.append(rand)

# Calculul valorilor proprii și polinomului caracteristic
valorile_proprii, polinom_caracteristic = calcul_valori_proprii_si_polinom_caracteristic(valori_matrice)

# Afișarea rezultatelor
print("\nMatrice:")
print(np.array(valori_matrice))
print("\nValorile proprii:", valorile_proprii)
print("Polinom caracteristic:", polinom_caracteristic)

