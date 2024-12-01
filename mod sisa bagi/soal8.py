angka = int(input("Masukkan sebuah angka: "))

if angka % 7 == 0 or angka % 11 == 0:
    print(f"{angka} adalah kelipatan 7 atau 11.")
else:
    print(f"{angka} bukan kelipatan 7 atau 11.")
