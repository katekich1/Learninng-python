x = int(input('masukan nilai pertama (x)\t: '))
y = int(input('masukan nilai pertama (y)\t: '))
z = int(input('masukan nilai pertama (z)\t: '))

# nilai terbesar
if x >= y and x >= z:
    terbesar = x
elif y >= x and y >= z:
    terbesar = y
else :
    terbesar = z

# nilai terkecil
if x <= y and x <= z:
    terkecil = x
elif y <= x and y <= z:
    terkecil = y
else :
    terkecil = z

# hasil nya
print ('nilai terbesar adalah\t: ' ,terbesar )
print ('nilai terkecil adalah\t: ' ,terkecil )