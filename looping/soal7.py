jumlah = 0
for x in range (1,7,2):
    if x <5:
        print(x,end=" + ")
    else:
        print(x,end=" = ")
    jumlah = jumlah + (x)
print(jumlah)