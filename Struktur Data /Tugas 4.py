# TEMPAT MENYIMPAN DATA (List di dalam List)

data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

# PERULANGAN SUPAYA MENU TERUS MUNCUL
while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")
    
  
    pilihan = input("Pilih menu 1-8: ").strip()

    # MENU 1: TAMPILKAN DATA
    if pilihan == "1":
        print("\n--- DAFTAR DATA MAHASISWA ---")
        
      
        if len(data_mahasiswa) == 0:
            print("Data mahasiswa masih kosong.")
        else:
            nomor = 1
            for mhs in data_mahasiswa:
                nama = mhs[0]
                nilai = mhs[1]
                print(str(nomor) + ". Nama: " + nama + " | Nilai: " + str(nilai))
                nomor = nomor + 1
        print("-----------------------------")

    # MENU 2: TAMBAH DATA
    elif pilihan == "2":
        print("\n--- TAMBAH DATA MAHASISWA ---")
        nama_baru = input("Masukkan nama mahasiswa: ")
        nilai_baru = int(input("Masukkan nilai mahasiswa: "))
        
      
        mahasiswa_baru = [nama_baru, nilai_baru]
        data_mahasiswa.append(mahasiswa_baru)
        print("Data berhasil ditambahkan!")

    # MENU 3: UBAH DATA
    elif pilihan == "3":
        print("\n--- UBAH DATA MAHASISWA ---")
        nama_cari = input("Masukkan nama mahasiswa yang mau diubah nilainya: ")
        
        ketemu = False
        for mhs in data_mahasiswa:
          
            if mhs[0].lower() == nama_cari.lower():
                nilai_baru = int(input("Masukkan nilai baru untuk " + mhs[0] + ": "))
                mhs[1] = nilai_baru 
                print("Nilai berhasil diubah!")
                ketemu = True
                break 
                
        if ketemu == False:
            print("Nama tidak ditemukan!")

    # MENU 4: HAPUS DATA
    elif pilihan == "4":
        print("\n--- HAPUS DATA MAHASISWA ---")
        nama_hapus = input("Masukkan nama mahasiswa yang mau dihapus: ")
        
        ketemu = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_hapus.lower():
                data_mahasiswa.remove(mhs) # .remove() untuk menghapus data dari list
                print("Data " + mhs[0] + " berhasil dihapus!")
                ketemu = True
                break
                
        if ketemu == False:
            print("Nama tidak ditemukan!")

    # MENU 5: CARI DATA
    elif pilihan == "5":
        print("\n--- CARI DATA MAHASISWA ---")
        nama_cari = input("Masukkan nama mahasiswa yang dicari: ")
        
        ketemu = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                print("Data Ketemu! -> Nama: " + mhs[0] + " | Nilai: " + str(mhs[1]))
                ketemu = True
                break
                
        if ketemu == False:
            print("Nama tidak ditemukan!")

    # MENU 6: URUTKAN DATA BERDASARKAN NILAI TERTINGGI
    elif pilihan == "6":
        print("\n--- DATA DIURUTKAN (NILAI TERTINGGI) ---")
        if len(data_mahasiswa) == 0:
            print("Data masih kosong.")
        else:
           
            data_salinan = list(data_mahasiswa)
            jumlah_data = len(data_salinan)
            
            
            for i in range(jumlah_data):
                for j in range(0, jumlah_data - 1):
                   
                    if data_salinan[j][1] < data_salinan[j + 1][1]:
                        wadah_tukar = data_salinan[j]
                        data_salinan[j] = data_salinan[j + 1]
                        data_salinan[j + 1] = wadah_tukar
            
            # Cetak hasil urutannya
            nomor = 1
            for mhs in data_salinan:
                print(str(nomor) + ". Nama: " + mhs[0] + " | Nilai: " + str(mhs[1]))
                nomor = nomor + 1

    # MENU 7: HITUNG RATA-RATA NILAI
    elif pilihan == "7":
        print("\n--- HITUNG RATA-RATA ---")
        if len(data_mahasiswa) == 0:
            print("Data kosong, rata-rata adalah 0")
        else:
            total_nilai = 0
           
            for mhs in data_mahasiswa:
                total_nilai = total_nilai + mhs[1]
            
            # Hitung rata-rata
            banyak_mahasiswa = len(data_mahasiswa)
            rata_rata = total_nilai / banyak_mahasiswa
            
            print("Total Mahasiswa : " + str(banyak_mahasiswa))
            print("Total Nilai     : " + str(total_nilai))
            print("Rata-rata Nilai : " + str(rata_rata))

    # MENU 8: KELUAR PROGRAM
    elif pilihan == "8":
        print("\nProgram selesai. Terima kasih!")
        break 

    # JIKA USER SALAH KETIK
    else:
        print("\nPilihan salah! Tolong ketik angka 1 sampai 8 saja.")
