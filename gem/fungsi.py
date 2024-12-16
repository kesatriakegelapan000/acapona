from masuk import *

def attack (hero,musuh):
	print(f"{hero.name} menyerang {musuh.name}")
	musuh.deff -= hero.attack
	print(f"{musuh.deff}")
	if musuh.deff <= 0 :
		print(f"{musuh.name} telah mati mengenaskan")

hero.play()

attack(hero,musuh)

