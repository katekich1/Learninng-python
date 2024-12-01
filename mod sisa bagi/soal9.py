angka_1 = int(input("Masukkan angka pertama: "))
angka_2 = int(input("Masukkan angka kedua: "))
angka_3 = int(input("Masukkan angka ketiga: "))

if angka_1 % 2 == 0 or angka_1 % 3 == 0 or angka_1 % 5 == 0:
    print(f"{angka_1} habis dibagi 2, 3, atau 5.")
elif angka_2 % 2 == 0 or angka_2 % 3 == 0 or angka_2 % 5 == 0:
    print(f"{angka_2} habis dibagi 2, 3, atau 5.")
elif angka_3 % 2 == 0 or angka_3 % 3 == 0 or angka_3 % 5 == 0:
    print(f"{angka_3} habis dibagi 2, 3, atau 5.")
else:
    print("Tidak ada angka yang habis dibagi 2, 3, atau 5.")
