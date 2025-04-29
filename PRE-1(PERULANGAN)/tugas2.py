# Meminta jumlah baris dari pengguna
rows = int(input("Masukkan jumlah baris: "))

# Loop untuk setiap baris
for i in range(rows):
    # Mencetak spasi sebelum bintang
    for j in range(rows - i - 1):
        print(" ", end="")
    
    # Mencetak bintang
    for j in range(2 * i + 1):
        print("*", end="")
    
    # Pindah ke baris berikutnya
    print()
