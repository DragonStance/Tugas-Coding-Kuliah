import math

# Input User
lat1 = float(input("Masukkan lintang kota 1: "))
lon1 = float(input("Masukkan bujur kota 1: "))
lat2 = float(input("Masukkan lintang kota 2: "))
lon2 = float(input("Masukkan bujur kota 2: "))

# Mengonversi derajat ke radian
lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

# Jari-jari bumi dalam kilometer
R = 6371.0

# Menghitung perbedaan lintang dan bujur
dlat = lat2 - lat1
dlon = lon2 - lon1

# Menggunakan rumus Haversine
a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Menghitung jarak
jarak = R * c

# Menampilkan hasil jarak
print(f"Jarak antara kedua titik tersebut adalah {jarak:.2f} kilometer.")