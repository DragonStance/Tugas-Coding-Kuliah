def is_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cek_prima():
    bilangan = int(input("Masukkan bilangan yang ingin diperiksa: "))
    
    if is_prima(bilangan):
        print(f"{bilangan} adalah bilangan prima.")
    else:
        print(f"{bilangan} bukan bilangan prima.")

cek_prima()