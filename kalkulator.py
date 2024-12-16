import os 

os.system("clear")

class Kalku :


 def __init__(self,no1,no2):
  self.no1 = float(no1)
  self.no2 = float(no2)
  self.hasil = None
 def hitung(self,aksi):
  if aksi == "+":
   self.hasil = self.no1 + self.no2 

  elif aksi == "-":
   self.hasil = self.no1 - self.no2

  elif aksi == "*":
   self.hasil = self.no1 * self.no2

  elif aksi == "/":
   if self.no2 != 0:
    self.hasil = self.no1 / self.no2

   else :
    self.hasil = "jangan input 0 lah kon***"

  else:
   self.hasil = "apcb"

 def __str__(self):
  return f"{self.hasil}"



print("""
----------------
KALKULATOR MEWING
-----------------
""")
a = input("masukan angka = ")
b = input("masukan angka = ")
c = input("masukan aksi (+-*/) = ")
d = Kalku(a,b)
d.hitung(c)


print(f"hasil = {d}")

