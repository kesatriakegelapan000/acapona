import random
import os
import time


os.system("clear")

class Apcb :


 def __init__(self,ia,ib):
  self.nama = ia
  self.antrian = ib


 def up(self,up):
  self.antrian += up

 def change(self,iv1,iv2):
  self.nama = iv1
  self.antrian = iv2

 def prin(self):
  print(self.nama)
  print(self.antrian)



a = Apcb("rian",10)

a.up(3)
a.change("akuaob","apcb")
a.prin()
a.change("gacor88",10)

time.sleep(2)

a.prin()

