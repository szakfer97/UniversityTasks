import tema3

class Mostenita:
  fisier1 = open("nume.txt","r")
  fisier2 = open("numenou.txt","r")
  print(fisier1.read() + " si " + fisier2.read() + " sunt miliardari")
  student = tema3.Persoana("Szakacsi Ferenc-Adam", "Informatica", 3, 180)
  student.prezinta()
  student.nrdecredite()
  if(student.andestudiu == 3):
    try:
        aniilafacultate = lambda an:an + 2
        print("Am petrecut " + str(aniilafacultate(1)) + " ani la facultate")
    except Exception as e:
        print("Am primit o exceptie,anume: " + str(e))        