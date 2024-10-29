harga_barang = float(input('masukan total harga barang\t: '))

diskon = 0
if harga_barang >= 100000 :
    diskon = harga_barang * 0.05
total_bayar = harga_barang - diskon

# total bayar
print ('anda mendapat diskon sebesar\t: ' ,diskon)
print ('total yang harus anda bayar sebesar\t: ' ,total_bayar)