# definisi function
def luasPersegi(p, l):
    return p * l


def main():
    panjang = float(input('Masukkan nilai panjang : '))
    lebar = float(input('Masukkan nilai Lebar : '))

    # Menggunakan function
    luas = luasPersegi(panjang, lebar)

    print('Luas persegi :', luas)


main()
