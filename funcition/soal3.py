def jumlah_kata(kalimat):
    return len(kalimat.split())

kalimat = input("Masukkan sebuah kalimat: ")

print(f"Jumlah kata dalam kalimat: {jumlah_kata(kalimat)}")
