panjang = float(input('Masukkan nilai panjang : '))

if(panjang < 0):
    panjang = panjang * -1
    print('Nilai panjang di ubah ke positif ', panjang)

lebar = float(input('Masukkan nilai Lebar : '))
if(lebar < 0):
    lebar = lebar * -1
    print('Nilai lebar di ubah ke positif ', lebar)

luas = panjang * lebar

print('Luas persegi :', luas)