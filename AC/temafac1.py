import numpy as np

def matrice_hermitica(matrice):
    return np.array_equal(matrice, np.conjugate(matrice).T)

ordin_matrice = int(input("Introduceti ordinul matricei: "))

valori_matrice = []
for i in range(ordin_matrice):
    rand = []
    for j in range(ordin_matrice):
        valoare_real = float(input(f"Introduceti partea reala pentru matrice[{i+1}][{j+1}]: "))
        valoare_imaginara = float(input(f"Introduceti partea imaginara pentru matrice[{i+1}][{j+1}]: "))
        valoare = valoare_real + 1j * valoare_imaginara
        rand.append(valoare)
    valori_matrice.append(rand)

matrice = np.array(valori_matrice)

if matrice_hermitica(matrice):
    print("Matricea este Hermitică.")
else:
    print("Matricea nu este Hermitică.")

