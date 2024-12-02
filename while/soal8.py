maks = None
while True:
    angka = int(input("Masukkan angka: "))
    if angka < 0:
        break
    if maks is None or angka > maks:
        maks = angka
print(f"Angka tertinggi: {maks}")
