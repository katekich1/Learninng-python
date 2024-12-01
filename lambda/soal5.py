kabisat = lambda tahun: (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

tahun = int(input("Masukkan tahun: "))

hasil = kabisat(tahun)
if hasil:
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
