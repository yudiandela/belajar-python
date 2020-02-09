panjang = float(input('Masukkan nilai panjang : '))
while panjang < 0:
    print('Anda memasukkan nilai negatif ulangi lagi!')
    panjang = float(input('Masukkan nilai panjang : '))

lebar = float(input('Masukkan nilai Lebar : '))
while lebar < 0:
    print('Anda memasukkan nilai negatif ulangi lagi!')
    lebar = float(input('Masukkan nilai lebar : '))

luas = panjang * lebar

print('Luas persegi :', luas)
