import numpy as np

def gauss_jordan(matrice_extinsa):
    n, m = matrice_extinsa.shape

    # Etapa Gauss-Jordan
    for pivot in range(min(n, m-1)):
        # Selectează pivotul nenul
        pivot_nenul = np.argmax(np.abs(matrice_extinsa[pivot:, pivot])) + pivot

        # Schimbă rândurile pentru a muta pivotul în poziția corespunzătoare
        matrice_extinsa[[pivot, pivot_nenul]] = matrice_extinsa[[pivot_nenul, pivot]]

        # Facem pivotul 1
        matrice_extinsa[pivot] = matrice_extinsa[pivot] / matrice_extinsa[pivot, pivot]

        # Eliminare în coloană
        for i in range(n):
            if i != pivot:
                matrice_extinsa[i] -= matrice_extinsa[i, pivot] * matrice_extinsa[pivot]

    return matrice_extinsa

# Introducerea ordinului matricei
ordin_matrice = int(input("Introduceti ordinul matricei: "))

# Introducerea valorilor matricei
valori_matrice = []
for i in range(ordin_matrice):
    rand = [float(input(f"Introduceti valoarea pentru matrice[{i+1}][{j+1}]: ")) for j in range(ordin_matrice)]
    valori_matrice.append(rand)

# Introducerea matricei identitate extinse
matrice_extinsa = np.hstack([np.array(valori_matrice), np.eye(ordin_matrice)])

# Aplicarea metodei Gauss-Jordan
matrice_redusa = gauss_jordan(matrice_extinsa)

# Extrage matricea inversă
matrice_inversa = matrice_redusa[:, ordin_matrice:]

# Calcularea rangului
rang = np.linalg.matrix_rank(np.array(valori_matrice))

# Afișarea rezultatelor
print(f"\nMatricea inițială:\n{np.array(valori_matrice)}")
print(f"\nMatricea inversă:\n{matrice_inversa}")
print(f"\nRangul matricei: {rang}")
