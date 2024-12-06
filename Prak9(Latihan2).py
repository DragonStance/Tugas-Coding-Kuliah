def buat_file(nama_file):
    print("Masukkan data untuk file")
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan tahun angkatanmu: ")
    with open(f"{nama_file}.txt", "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"NIM: {nim}\n")
        file.write(f"Angkatan: {angkatan}\n")
    print("File Berhasil Dibuat\n")


def baca_file(nama_file):
    try:
        with open(f"{nama_file}.txt", "r") as file:
            print("\nIsi file:")
            print(file.read())
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file sudah dibuat sebelumnya.\n")


def tambah_file(nama_file):
    try:
        tambahan = input("Masukkan teks yang ingin ditambahkan: ")
        with open(f"{nama_file}.txt", "a") as file:
            file.write(tambahan + "\n")
        print("Data berhasil ditambahkan ke file.\n")
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file sudah dibuat sebelumnya.\n")


def main():
    while True:
        print("===== Program File Handling =====")
        print("1. Membuat dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Text Pada File")
        print("4. Keluar Dari Program")
        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

        if pilihan == "1":
            nama_file = input("Masukkan Nama File: ")
            buat_file(nama_file)
        elif pilihan == "2":
            nama_file = input("Masukkan Nama File: ")
            baca_file(nama_file)
        elif pilihan == "3":
            nama_file = input("Masukkan Nama File: ")
            tambah_file(nama_file)
        elif pilihan == "4":
            print("Program Selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1/2/3/4.\n")

main()
