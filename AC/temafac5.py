import numpy as np

def este_triunghiulara(matrice):
    return np.allclose(matrice, np.triu(matrice)) or np.allclose(matrice, np.tril(matrice))

def inversa_triunghiulara(matrice):
    try:
        inversa = np.linalg.inv(matrice)
        return inversa
    except np.linalg.LinAlgError:
        print("Matricea nu este inversabila.")
        return None

def este_inversa_triunghiulara(matrice, inversa):
    return este_triunghiulara(inversa)

# Introducere matrice
ordin_matrice = int(input("Introduceti ordinul matricei: "))
valori_matrice = np.zeros((ordin_matrice, ordin_matrice))

for i in range(ordin_matrice):
    for j in range(ordin_matrice):
        valoare = float(input(f"Introduceti valoarea pentru matrice[{i+1}][{j+1}]: "))
        valori_matrice[i, j] = valoare

matrice = valori_matrice

# Calcul inversa
inversa = inversa_triunghiulara(matrice)

if inversa is not None:
    # Verifica daca inversa este triunghiulara
    if este_inversa_triunghiulara(matrice, inversa):
        print("Inversa matricei este tot triunghiulara.")
    else:
        print("Inversa matricei nu este triunghiulara.")
