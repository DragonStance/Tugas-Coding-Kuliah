print("Hitung Luas Ruangan")

panjang_ruang = float(input("Masukkan Panjang Ruangan: "))
lebar_ruang = float(input("Masukkan Lebar Ruangan: "))
satuan = input("Masukkan Satuan (Meter/Inci): ")
hasil_perhitungan = panjang_ruang * lebar_ruang

print(f"Luas ruangan dengan panjang {panjang_ruang} dan lebar {lebar_ruang} adalah {hasil_perhitungan} {satuan}")