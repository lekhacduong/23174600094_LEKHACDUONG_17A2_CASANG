U = 220
I = 1.5
P = U * I
so_gio = int(input("Nhập số giờ sử dụng máy lọc không khí: "))
A = P * so_gio
so_tien_dien = 5000 * A
print(f"Số tiền điện phải trả là: {so_tien_dien}")