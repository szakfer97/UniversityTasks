import numpy as np

def gauss_jordan(matrice_extinsa):
    n, m = matrice_extinsa.shape
    for pivot in range(min(n, m-1)):
        pivot_nenul = np.argmax(np.abs(matrice_extinsa[pivot:, pivot])) + pivot
        matrice_extinsa[[pivot, pivot_nenul]] = matrice_extinsa[[pivot_nenul, pivot]]
        matrice_extinsa[pivot] = matrice_extinsa[pivot] / matrice_extinsa[pivot, pivot]
        for i in range(n):
            if i != pivot:
                matrice_extinsa[i] -= matrice_extinsa[i, pivot] * matrice_extinsa[pivot]
    return matrice_extinsa

ordin_matrice = int(input("Introduceti ordinul matricei: "))
valori_matrice = []
for i in range(ordin_matrice):
    rand = [float(input(f"Introduceti valoarea pentru matrice[{i+1}][{j+1}]: ")) for j in range(ordin_matrice)]
    valori_matrice.append(rand)
matrice_extinsa = np.hstack([np.array(valori_matrice), np.eye(ordin_matrice)])
matrice_redusa = gauss_jordan(matrice_extinsa)
matrice_inversa = matrice_redusa[:, ordin_matrice:]
rang = np.linalg.matrix_rank(np.array(valori_matrice))
print(f"\nMatricea inițială:\n{np.array(valori_matrice)}")
print(f"\nMatricea inversă:\n{matrice_inversa}")
print(f"\nRangul matricei: {rang}")

