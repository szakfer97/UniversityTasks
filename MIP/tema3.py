import datetime

class Persoana:
  def __init__(self, nume, specializare, andestudiu ,credite):
    self.nume = nume
    self.specializare = specializare
    self.andestudiu = andestudiu
    self.credite = credite
  def prezinta(self):
    print("Prezinta " + self.nume + ",student " + self.specializare + " anul " + str(self.andestudiu) + ",acum la " + str(datetime.datetime.now()))
  def nrdecredite(self):
    print("Daca termin facultatea,voi avea " + str(self.credite) + " de credite")    