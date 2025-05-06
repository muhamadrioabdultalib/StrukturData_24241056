# cara membuat tuple 

t = (1234, 'Hello World')
t1 = (1, 2, 3)
t2 = "a", "b", "c"        # Tanpa tanda kurung juga valid
t3 = ()                   # Tuple kosong
t4 = (5,)                 # Tuple satu elemen (perlu koma!)

# membuat tuple singleton 
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))

# imdexing dan slicing tuple

# membuat tuple
nama = ('alief', 'hikham', 'pratama')

# mengakses indeks ke 1 dari tuple
print(nama[1])

# Membuat Tuple
t = (1, 5, 10, 15)

# mengubah isi elemen tuple
t = (1, 5, 10, 15)
temp_list = list(t)   # ubah tuple menjadi list
temp_list[0] = 0      # ubah elemen
t = tuple(temp_list)  # ubah kembali menjadi tuple
print(t)              # Output: (0, 5, 10, 15)

# membuat tuple
angka = (10, 20, 30, 40)

# Memotong tuple
print(angka[1:3]) 
print(angka[:2])
print(angka[2:])

# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)

# Tuple Bersarang (Nested Tuple)
t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mau", "pinjem"
tuple2 = "uang", 3, "juta boleh"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)

# tuple berisi list
t = ([1,2,3,4], True)

print (t)

# mula-mula kita buat tuple seperti ini
web = 123, "PTI UNDIKMA", "https://fsttundikma.id"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)