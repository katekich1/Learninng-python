def cek_huruf(huruf):
    huruf = huruf.upper()

    vokal = "AEIOU"

    if huruf.isalpha() and len(huruf) == 1:
        if huruf in vokal:
            return "Huruf tersebut adalah vokal."
        else:
            return "Huruf tersebut adalah konsonan."
    else:
        return "bukan berupa huruf."

input_huruf = input("Masukkan suatu huruf dari A-Z: ")
hasil = cek_huruf(input_huruf)
print(hasil)