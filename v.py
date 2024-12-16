import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    percobaan = 0

    print("Tebak angka antara 1 dan 100!")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"Selamat! Anda menebak angka {angka_rahasia} dalam {percobaan} percobaan.")

tebak_angka()
