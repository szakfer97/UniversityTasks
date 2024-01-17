import numpy as np

def este_triunghiulara(matrice):
    return np.allclose(matrice, np.triu(matrice)) or np.allclose(matrice, np.tril(matrice))

def produs_triunghiular(matrice1, matrice2):
    # Calculul produsului matricilor
    produs = np.dot(matrice1, matrice2)

    # Verificare dacă produsul este triunghiular
    return este_triunghiulara(produs)

# Introducere dimensiuni matrici
ordin_matrice = int(input("Introduceti ordinul matricilor: "))

# Introducere valori pentru prima matrice
matrice1 = np.zeros((ordin_matrice, ordin_matrice))
print("Introduceti valori pentru prima matrice:")
for i in range(ordin_matrice):
    for j in range(i, ordin_matrice):
        valoare = float(input(f"Introduceti valoarea pentru matrice1[{i+1}][{j+1}]: "))
        matrice1[i, j] = valoare

# Introducere valori pentru a doua matrice
matrice2 = np.zeros((ordin_matrice, ordin_matrice))
print("Introduceti valori pentru a doua matrice:")
for i in range(ordin_matrice):
    for j in range(i, ordin_matrice):
        valoare = float(input(f"Introduceti valoarea pentru matrice2[{i+1}][{j+1}]: "))
        matrice2[i, j] = valoare

# Verificare dacă produsul este triunghiular
if produs_triunghiular(matrice1, matrice2):
    print("Produsul matricilor este tot triunghiular.")
else:
    print("Produsul matricilor nu este triunghiular.")
