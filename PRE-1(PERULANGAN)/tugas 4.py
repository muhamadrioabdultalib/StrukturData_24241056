# variabel global untuk menyimpan data buku
mahasiswa = []

# Fungsi untuk menampilkan semua data buku
def show_data():
    if len(mahasiswa) <=0 :
        print("DATA MAHASISWA BELUM ADA")
    else:
        for indeks in range(len(mahasiswa)):
            print("[%d] %s" % (indeks, mahasiswa[indeks]))
            
def insert_data():
    mahasiswa_baru = input("Nama Mahasiswa : ")
    mahasiswa.append(mahasiswa_baru)
    
def edit_data():
    show_data()
    indeks = int(input("Inputkan NIM Mahasiswa : "))
    if(indeks > len(mahasiswa)):
        print("NIM Mahasiswa Tidak Ditemukan")
    else:
        Mahasiswa_Baru = input("Nama Mahasiswa : ")
        mahasiswa[indeks] = Mahasiswa_Baru
        
def delete_data():
    show_data()
    indeks = int(input("Inputkan NIM Mahasiswa : "))
    if(indeks > len(mahasiswa)):
        print("NIM Mahasiswa Tidak Ditemukan")
    else:
        mahasiswa.remove(mahasiswa[indeks])
        print(f"Mahasiswa Dengan NIM {indeks} Terhapus")
        
def show_menu():
    print("\n")
    print(5*"-","MENU", 5*"-")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("PILIH MENU : "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Pilihan Anda Salah!")
        
if __name__ == "__main__":
    while(True):
        show_menu()