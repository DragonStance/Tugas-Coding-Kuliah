def tampilkan_ordinal(angka):
    if angka % 100 in [11, 12, 13]:
        suffix = "th"
    elif angka % 10 == 1:
        suffix = "st"
    elif angka % 10 == 2:
        suffix = "nd"
    elif angka % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    
    print(f"{angka}{suffix}")

while True:
    angka = int(input("Masukkan angka (Ketik 0 untuk menghentikan program): "))
    if angka <= 0:
        print("Terimakasih telah menggunakan program saya.")
        break;
    else: tampilkan_ordinal(angka)