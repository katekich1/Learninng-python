def elemen_terbesar(lst):
    return max(lst)

list_angka = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))

print(f"Elemen terbesar dalam list: {elemen_terbesar(list_angka)}")
