def cek_ganjil(n):
    if n % 2 != 0:
        return True
    return False

angka = 7
if cek_ganjil(angka):
    print(f"{angka} adalah bilangan ganjil.")
else:
    print(f"{angka} bukan bilangan ganjil.")