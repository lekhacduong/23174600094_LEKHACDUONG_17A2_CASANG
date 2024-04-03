tong = 0
so_le = " "
so_chan = " "
so_luong_so_nguyen = 0
cac_so_da_nhap = " "

while tong <= 1000:
    n = int(input("Nhập số nguyên dương: "))
    tong += n
    so_luong_so_nguyen += 1
    cac_so_da_nhap += str(n) + " "
    if n % 2 == 0:
        so_chan += str(n) + " "
    else:
        so_le += str(n) + " "

print("Các só đã nhập từ bàn phím là: ",cac_so_da_nhap)
print("Các số lẻ đã nhập là: ",so_le)
print("Các số chẵn đã nhập là: ",so_chan)
print("Số lượng số nguyên đã nhập là: ",so_luong_so_nguyen)
        
