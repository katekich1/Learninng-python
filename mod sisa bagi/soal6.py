angka = int(input("Masukkan sebuah angka: "))

if angka % 3 == 0 and angka % 4 == 0:
    print(f"{angka} adalah kelipatan dari 3 dan 4.")
else:
    print(f"{angka} bukan kelipatan dari 3 dan 4.")
