lebih_besar = lambda a, b: a if a > b else b

angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))

hasil = lebih_besar(angka_1, angka_2)
print("Angka yang lebih besar adalah:", hasil)
