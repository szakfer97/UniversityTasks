nrdeteme = 2
while nrdeteme <= 15:
    print(str(nrdeteme) + " teme")
    nrdeteme +=1
listafructe = ["banane","mere","struguri","caise","ananas"]
for fruct in listafructe:
    print(fruct)
tuplucosdecumparaturi = ["fructe","legume","carne","branzeturi","dulciuri"]
print(tuplucosdecumparaturi)    
setdematerii = ["Grafica pe calculator","Sisteme de operare","Medii si instrumente de programare","Calcul numeric"]
print(setdematerii)
dictionarSarbatori = {
    "Februarie": "Ziua indragostitilor",
    "Aprilie": "Paste",
    "Decembrie":"Craciun"
}
print(dictionarSarbatori["Aprilie"])
nume1 = "Ferenc"
nume2 = "Adam"
print("Numele meu este " + nume1 + "-" + nume2)
prezinta = True
ziuadenastere = False 
if(prezinta):
    print(nume1 + "-" + nume2 + " prezinta la ora")
if(not ziuadenastere):
    print("E ziua de nastere a lui " + nume1 + "-" + nume2)
else:
    print("Nu e ziua de nastere a lui " + nume1 + "-" + nume2)            