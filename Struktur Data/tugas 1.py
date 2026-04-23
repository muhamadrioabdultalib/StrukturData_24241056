nama = input("Masukan nama anda : ")


print("selamat datang", nama)

umur = int(input("Masukan umur anda : "))

if umur >= 60:
    print("banyakin ibadah, bentar lagi mati")
elif umur <= 0:
    print("anda belum lahir")
elif umur >= 18:
    print("anda cukup umur")
else:
    print("anda belum cukup umur")

print("Program selesai")