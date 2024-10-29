siswa = str(input('masukan nama siswa\t: '))
nilai = int(input('masukan nilai siswa (0-100)\t: '))

if 90 <= nilai <= 100:
    print ('A')
elif 80 <= nilai <= 90:
    print ('B')
elif 70 <= nilai <= 80:
    print ('C')
elif 60 <= nilai <= 70:
    print ('D')
elif 0 <= nilai <= 60:
    print ('E')
else :
    print ('anda salah')

