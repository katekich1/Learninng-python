def lingkaran():
    print("=" *30)
    print("\tRUMUS LINGKARAN")
    print("=" *30)

    PHI = 3.14
    r = int(input("masukan nilai jari jari\t: "))

    l = lambda r: PHI * r * r
    k = lambda r: PHI * 2 * r 

    print("luas lingkaran\t\t:" ,l(r))
    print("keliling lingkaran\t\t:" ,k(r))

lingkaran()
