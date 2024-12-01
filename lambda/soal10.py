pembagian = lambda a, b: a / b if b != 0 else None

angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))

hasil = pembagian(angka_1, angka_2)
if hasil is None:
    print("Tidak bisa membagi dengan nol.")
else:
    print(f"Hasil pembagian: {hasil}")
