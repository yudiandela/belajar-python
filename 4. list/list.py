# Basic list
data = [1, 2, 3, 4, 5]
print(data[1])  # menampilkan data dengan index ke 1

# Intermediate List
dataList = []
jumlahData = int(input('Masukkan jumlah data yang akan di input : '))

for i in range(jumlahData):
    dataList.append(int(input('Masukkan data : ')))

counter = 0
for i in range(len(dataList)):
    if dataList[i] >= 60:
        counter += 1

# Menampilkan data input yang lebih besar atau sama dengan 60
print('Jumlah yang lulus : ', counter)

# Menampilkan jumlah data di dalam List
print('Jumlah dataList : ', len(dataList))
