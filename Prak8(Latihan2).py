def perpangkatan(base, power):
    if power == 0: 
        return 1
    elif power > 0: 
        return base * perpangkatan(base, power - 1)
    else: 
        return 1 / perpangkatan(base, -power)

print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")

while True:
    base_input = input("Masukkan Angka: ")
    if base_input == "":
        print("Program Selesai")
        break

    base = int(base_input)
    power = int(input("Masukkan Pangkatnya: "))
    hasil = perpangkatan(base, power)

    print(f"Hasilnya adalah: {hasil}\n")