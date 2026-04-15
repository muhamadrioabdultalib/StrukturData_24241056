# Input nama
nama = input("Masukkan nama anda: ")

# Cek nama (tidak boleh kosong)
if nama != "":
    print("Nama benar, lanjut ke program berikutnya")
else:
    print("Silahkan coba lagi")
    exit()

# Input angka
angka = int(input("Masukkan angka (1-10): "))

# Menampilkan tabel perkalian
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")