# class
class Persegi():
    # field
    panjang = 0
    lebar = 0

    # method
    def hitungLuas(self):
        return self.panjang * self.lebar


# object
def main():
    persegiEmpat = Persegi()
    persegiEmpat.panjang = float(input('Masukkan ukuran panjang : '))
    persegiEmpat.lebar = float(input('Masukkan ukuran lebar : '))
    luas = persegiEmpat.hitungLuas()

    print(luas)


main()
