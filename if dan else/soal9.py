suhu = float(input("Masukkan suhu dalam derajat Celsius: "))

if suhu > 30:
    print("Panas")
elif 20 <= suhu <= 30:
    print("Normal")
else:
    print("Dingin")
