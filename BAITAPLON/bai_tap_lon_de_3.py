# gọi hàm:
import csv
import random

# khởi tạo các giá trị:
do_dai = 500
so_ngua = 5

xac_suat_di_chuyen = [0.2, 0.3, 0.1, 0.4, 0.25]

vi_tri = [0] * so_ngua
khoang_cach_di_chuyen = [0] * do_dai

# mô phỏng cuộc đua: 
for i in range(do_dai):
    for j in range(so_ngua):
        if random.random() < xac_suat_di_chuyen[j]:
            vi_tri[j] += 1
            khoang_cach_di_chuyen[vi_tri[j] - 1 ] += 1
    
    if all(vi_tri[j] == do_dai for j in range(so_ngua)):
        break

# thao tác với file csv: 
file = open('dua_ngua.csv', 'w', newline = '', encoding = 'utf-8') 
write = csv.writer(file)
write.writerow(['Vị trí','Mã ngựa','Khoảng cách di chuyển'])
for j in range(so_ngua):
    for i in range(vi_tri[j]):
        write.writerow([i + 1, j + 1, khoang_cach_di_chuyen[i]])
file.close()

# in kết quả:
for j in range(so_ngua):
    print(f'Ngựa {j + 1} : Vị trí về đích là: {vi_tri[j]}')
                