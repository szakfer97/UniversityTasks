def calculare_ordin_si_divizori(n, element):
    ordin = 1
    rezultat = element % n
    divizori_zero = []

    while rezultat != 1:
        ordin += 1
        rezultat = (rezultat * element) % n
        if rezultat == 0:
            divizori_zero.append(element)

    return ordin, divizori_zero

n = int(input("Introduceți n (ordinea grupului resturilor modulo n): "))
element = int(input("Introduceți elementul pentru care doriți să calculați ordinul: "))

ordin, divizori_zero = calculare_ordin_si_divizori(n, element)

print(f"Ordinul elementului {element} în grupul resturilor modulo {n} este: {ordin}")
print(f"Divizorii de zero ai lui {n} sunt: {divizori_zero}")

