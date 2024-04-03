import math

while True:
    so_1 = float(input("Nhập số thứ nhất: "))
    so_2 = float(input("Nhập số thứ hai: "))
    
    tong = so_1 + so_2
    hieu1 = so_1 - so_2
    hieu2 = so_2 - so_1
    tich = so_1 * so_2
    thuong1 = so_1 / so_2
    thuong2 = so_2 / so_1
    luy_thua_1 = so_1 ** 2
    luy_thua_2 = so_2 ** 2
    can_1 = math.sqrt(so_1)
    can_2 = math.sqrt(so_2)
    
    print("Số thứ nhất là: ", so_1)
    print("Số thứ hai là: ", so_2)
    print("Tổng 2 số: ", tong)
    print("Hiệu số thứ nhất trừ số thứ hai: ", hieu1)
    print("Hiệu số thứ hai trừ số thứ nhất: ", hieu2)
    print("Tích hai số là: ", tich)
    print("Thương của số thứ nhất chia số thứ hai là: ", thuong1)
    print("Thương của số thứ hai chi số thứ nhất là: ", thuong2)
    print("Lũy thừa số thứ nhất là: ", luy_thua_1)
    print("Lũy thừa số thứ hai là: ", luy_thua_2)
    print("Căn bậc 2 số thứ nhất là: ", can_1)
    print("Căn bậc 2 số thứ hai là: ", can_2)

    print("\n")
    
    print('''Bạn có muốn tiếp tục không?
                  1.Có
                  2.Không
        ''')
    
    choose = int(input("Nhập lựa chọn: "))
    if choose == 1:
        continue
    elif choose == 2:
        break
    else:
        print("Vui lòng nhập lại lựa chọn!")
