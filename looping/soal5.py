jumlah = 0
for x in range (5):
    jumlah = jumlah + (x + 1)
    print (x + 1, end= ' ')
    if x <= 3:
        print("+", end=" ")
print ('=' ,jumlah)