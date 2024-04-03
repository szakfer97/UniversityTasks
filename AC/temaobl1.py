import numpy as np
from sympy import symbols, Matrix, solve

def calcul_valori_proprii_si_polinom_caracteristic(matrice):
    x = symbols('x')

    polinom_caracteristic = (Matrix(matrice) - x * np.eye(len(matrice))).det()

    valorile_proprii = solve(polinom_caracteristic, x)
    
    return valorile_proprii, polinom_caracteristic

ordin_matrice = int(input("Introduceti ordinul matricei (2 sau 3): "))

valori_matrice = []
for i in range(ordin_matrice):
    rand = []
    for j in range(ordin_matrice):
        valoare = float(input(f"Introduceti valoarea pentru matrice[{i+1}][{j+1}]: "))
        rand.append(valoare)
    valori_matrice.append(rand)

valorile_proprii, polinom_caracteristic = calcul_valori_proprii_si_polinom_caracteristic(valori_matrice)

print("\nMatrice:")
print(np.array(valori_matrice))
print("\nValorile proprii:", valorile_proprii)
print("Polinom caracteristic:", polinom_caracteristic)

