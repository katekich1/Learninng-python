import math

r = float(input("Masukkan jari-jari tabung (dalam satuan panjang): "))
t = float(input("Masukkan tinggi tabung (dalam satuan panjang): "))

volume = 2 * math.pi * (r**2) * t

luas_permukaan = math.pi * (r**2) + 2 * math.pi * r * t

print("\n--- Hasil Perhitungan Geometri Tabung ---")
print(f"Jari-jari tabung: {r} satuan panjang")
print(f"Tinggi tabung: {t} satuan panjang")
print(f"Volume tabung: {volume:.2f} satuan kubik")
print(f"Luas permukaan tabung: {luas_permukaan:.2f} satuan persegi")
