import math
nilai1 = int(input("Masukkan Nilai A = "))
nilai2 = int(input("Masukkan Nilai B = "))
nilai3 = int(input("Masukkan Nilai C = "))

if nilai1 == 0:
    print("Bukan merupakan Persamaan Kuadrat")
else:
    D = (nilai2**2) - (4*nilai1*nilai3)

    if D > 0:
        x1 = (-nilai2 + math.sqrt(D)) / (2*nilai1)
        x2 = (-nilai2 - math.sqrt(D)) / (2*nilai1)
        print("Persamaan kuadrat: ", nilai1, "x^2 +", nilai2, "x +", nilai3)
        print("Determinan = ", D)
        print("Akar x1 = ", x1)
        print("Akar x2 = ", x2)
        print("Dua akar berbeda")

    elif D == 0:
        x1 = -nilai2 / (2*nilai1)
        print("Persamaan kuadrat: ", nilai1, "x^2 +", nilai2, "x +", nilai3)
        print("Determinan = ", D)
        print("Akar = ", x1)
        print("Dua akar sama")

    else:
        print("Persamaan kuadrat: ", nilai1, "x^2 +", nilai2, "x +", nilai3)
        print("Determinan = ", D)
        print("Akar x1 = -", (nilai2), "+ √", abs(D), "i / 2*", (nilai1))
        print("Akar x2 = -", (nilai2), "- √", abs(D), "i / 2*", (nilai1))
        print("Tidak punya akar real (akar imajiner)")