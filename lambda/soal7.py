terbalik = lambda lst: lst[::-1]

list_input = input("Masukkan elemen list (pisahkan dengan spasi): ").split()

hasil = terbalik(list_input)
print("List dalam urutan terbalik:", hasil)
