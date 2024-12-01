genap = lambda x: x % 2 == 0

angka = int(input("Masukkan sebuah angka: "))

hasil = genap(angka)
if hasil:
    print("Angka tersebut adalah genap.")
else:
    print("Angka tersebut adalah ganjil.")
