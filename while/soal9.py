jumlah = 0
while True:
    angka = int(input("Masukkan angka (masukkan angka negatif untuk berhenti): "))
    if angka < 0:
        break
    jumlah += angka
print(f"Jumlah angka: {jumlah}")
