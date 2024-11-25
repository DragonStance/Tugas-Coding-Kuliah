def tulis_biodata():
    nama = input("Masukkan Nama mu: ")
    umur = input("Masukkan Umur mu: ")
    alamat = input("Masukkan Alamatmu: ")
    email = input("Masukkan Emailmu: ")
    dosen = input("Masukkan Dosen Walimu: ")

    with open("Biodata.txt", "w") as file:
        file.write(f"Nama  : {nama}\n")
        file.write(f"Umur  : {umur}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email : {email}\n")
        file.write(f"Dosen Wali: {dosen}\n")
    print("\nData telah berhasil disimpan ke dalam file 'Biodata.txt'.")

def baca_biodata():
    file = open("Biodata.txt", "r") 
    isi_file = file.read()  
    file.close()  

    print("\nBerikut ini biodata kamu:\n")
    print(isi_file)

if __name__ == "__main__":
    tulis_biodata()

    baca_biodata()
