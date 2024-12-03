

import random
import os

os.system("clear")

print("\n\nPilih sisi koin\n1. Kepala\n2. Ekor")

try:
 pilih = int(input("\n\n Pilhan: "))
except:
 print("\n\nHarap masukan input yang valid(1 atau 2)")

hasil = random.choice([1,2])

if pilih == hasil:
 print("\n\nAnda menang!")
else:
 print("\n\nAnda kalah, adios.")
