def daftar_belanja():
    daftar = []

    while True:
        print("\nDaftar Belanja:")
        for item in daftar:
            print(f"- {item}")

        print("\nPilih opsi:")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            item = input("Masukkan nama item yang ingin ditambahkan: ")
            daftar.append(item)
        elif pilihan == '2':
            item = input("Masukkan nama item yang ingin dihapus: ")
            if item in daftar:
                daftar.remove(item)
            else:
                print("Item tidak ditemukan dalam daftar.")
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

daftar_belanja()
