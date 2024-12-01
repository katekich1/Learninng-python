jumlah_panjang = lambda words: sum(len(word) for word in words)

list_kata = input("Masukkan beberapa kata (pisahkan dengan spasi): ").split()

hasil = jumlah_panjang(list_kata)
print("Jumlah panjang kata-kata dalam list:", hasil)
