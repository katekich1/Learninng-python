import math

def hitung_volume_tabung(r, t):
    return math.pi * r**2 * t

def hitung_luas_permukaan_tabung(r, t):
    return 2 * math.pi * r * (r + t)

r = float(input("Masukkan jari-jari alas tabung (r): "))
t = float(input("Masukkan tinggi tabung (t): "))

volume = hitung_volume_tabung(r, t)
luas_permukaan = hitung_luas_permukaan_tabung(r, t)

print(f"Volume tabung: {volume:.2f} satuan kubik")
print(f"Luas permukaan tabung: {luas_permukaan:.2f} satuan persegi")