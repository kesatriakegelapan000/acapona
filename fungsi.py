import random
import os

os.system("clear")

class fungsi :
    def __init__ (self, inname, indarah, indampak):
        self.nama = inname
        self.darah = indarah
        self.dampak = indampak

    def fight(self, dmg):
        self.darah -= dmg
        print(f"{self.nama} menerima serangan sebesar {dmg} dan memiliki darah {self.darah}.")

    def __str__(self):
        return f"Nama: {self.nama}, Darah: {self.darah}, Dampak: {self.dampak}"

a = fungsi("elmanuk", 100, 10)
print(a)
a.fight(20)
print(a)
