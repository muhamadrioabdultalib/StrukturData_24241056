# Perulangan (Loop)

# for kondisi: JIKA KONDISI TERPENUHI
#    aksi JALANKAN AKSI

angka_list = [0, 2, 4, 8, 10]
print(angka_list)

# angka = 0
# print(angka)
# angka += 1 angka = angka + 1
# print(angka)
# angka += 1
# print(angka)

# for loop 
for i in angka_list:
    print(f"i sekarang -> {i}")
    
print("loop berakhir \n")    

# dengan range
angka_range = range(5)
for i in angka_range:
    print(f"i sekarang -> {i}")
    
print("loop berakhir \n")    

angka_range = range(1,10)
for i in angka_range:
    print(f"i sekarang -> {i}")
    
print("loop berakhir \n")

for i in range(1,4):
    print("*" * i)

