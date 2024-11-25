def penjumlahan_berurut(jumlah, i=1, total=0):
    if i > jumlah: 
        return total
    else:
        angka = float(input(f"Masukkan angka ke-{i}: "))
        return penjumlahan_berurut(jumlah, i + 1, total + angka)

jumlah = int(input("Masukkan Jumlah: "))

hasil = penjumlahan_berurut(jumlah)
print("Hasil penjumlahan berturut adalah:", hasil)