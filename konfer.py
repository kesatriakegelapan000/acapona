import pandas as pd

data = {}

def tambah_data():
    while True:
        kunci = input("Masukkan kunci (atau ketik 'exit' untuk keluar): ")
        if kunci.lower() == 'exit':
            break
        
        nilai = input(f"Masukkan nilai untuk '{kunci}': ")
        
        # Jika kunci sudah ada, tambahkan nilai ke list
        if kunci in data:
            data[kunci].append(nilai)
        else:
            data[kunci] = [nilai]  # Buat list baru jika kunci belum ada
        
        print(f"Data '{kunci}: {nilai}' telah ditambahkan.")

tambah_data()

print("\nData akhir dalam dictionary:")
print(data)

# Mengubah dictionary menjadi DataFrame
# Menggunakan list of dictionaries untuk membuat DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

print("\nData dalam DataFrame:")
print(df)

# Menyimpan DataFrame ke file Excel
df.to_excel('data.xlsx', index=False)

print("Data telah disimpan ke 'data.xlsx'.")
print(f"\n\n{'kalo gw malu tuh':^10}\n\n")
