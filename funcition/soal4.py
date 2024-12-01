def perbandingan_angka(angka1, angka2):
    if angka1 > angka2:
        return "Angka pertama lebih besar"
    elif angka1 < angka2:
        return "Angka kedua lebih besar"
    else:
        return "Kedua angka sama"

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

print(perbandingan_angka(angka1, angka2))
