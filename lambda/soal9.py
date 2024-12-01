kelipatan_3 = lambda x: x % 3 == 0

angka = int(input("Masukkan sebuah angka: "))

hasil = kelipatan_3(angka)
if hasil:
    print(f"{angka} adalah kelipatan dari 3.")
else:
    print(f"{angka} bukan kelipatan dari 3.")
