class Mahasiswa:
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

    def tampilkan_biodata(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Angkatan: {self.angkatan}")

def main():
    print("Masukkan Data Mahasiswa")
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan Tahun Angkatanmu: ")
    mahasiswa = Mahasiswa(nama, nim, angkatan)

    print("\nBiodata Mahasiswa:")
    mahasiswa.tampilkan_biodata()

    print("\nTotal Mahasiswa: 1") 
main()
