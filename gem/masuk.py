import os
import time


class Orang:

        def __init__(self,name,attack,deff):
                self.name = name
                self.attack = attack
                self.deff = deff

        def play (self):
                print(f"""
======================
  welcome to athanor
======================
name = {self.name}
attack = {self.attack}
deff = {self.deff}
""")

nama = input("nama = ")

hero = Orang(nama,88,25)

musuh = Orang("mewing",50,10)


