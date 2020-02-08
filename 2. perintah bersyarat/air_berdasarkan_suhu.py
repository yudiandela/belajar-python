suhu = float(input('Masukkan suhu air : '))

if(suhu <= 0):
    print('Air Beku')
elif(suhu > 0 and suhu <= 31):
    print('Air Dingin')
elif(suhu > 31 and suhu <= 61):
    print('Air Hangat')
elif(suhu > 61 and suhu < 100):
    print('Air Panas')
elif(suhu == 100):
    print('Air Mendidih')
else:
    print('Uap Air')