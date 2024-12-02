jumlah = 0
count = 0
while True:
    angka = int(input("Masukkan angka (masukkan angka negatif untuk berhenti): "))
    if angka < 0:
        break
    jumlah += angka
    count += 1
if count > 0:
    rata_rata = jumlah / count
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang dimasukkan.")
