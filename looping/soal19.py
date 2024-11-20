n = int(input("masukan jumlah nilai\t: "))

nilai = [ ]

for i in range(n):
    nilai_input = float(input(f"masukan nilai ke-{i+1}: "))
    nilai.append(nilai_input)

jumlah = sum(nilai)
rata_rata = jumlah / n

print(f"jumlah nilai: {jumlah}")
print(f"rata rata nilai: {rata_rata}")