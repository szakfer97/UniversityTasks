import numpy as np

def matrice_simetrica_antisimetrica(matrice):
    S = (matrice + matrice.T) / 2
    A_s = (matrice - matrice.T) / 2
    return S, A_s

ordin_matrice = int(input("Introduceti ordinul matricei pătratice: "))
valori_matrice = np.zeros((ordin_matrice, ordin_matrice))

for i in range(ordin_matrice):
    for j in range(ordin_matrice):
        valoare = float(input(f"Introduceti valoarea pentru matrice[{i+1}][{j+1}]: "))
        valori_matrice[i, j] = valoare

matrice = valori_matrice
S, A_s = matrice_simetrica_antisimetrica(matrice)

print("\nMatricea originala:")
print(matrice)
print("\nMatricea simetrica (S):")
print(S)
print("\nMatricea antisimetrica (A_s):")
print(A_s)
print("\nVerificare: A = S + A_s")
print("Rezultat:", np.allclose(matrice, S + A_s))
