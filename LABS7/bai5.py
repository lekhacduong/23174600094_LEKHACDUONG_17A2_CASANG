kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}
gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

# tinh hoa don: 
hoa_don = {}

tong_so_tien = 0
for mat_hang, so_luong in kho.items():
    don_gia = gia_tien[mat_hang]
    if so_luong > 0:
        so_luong_mua = min(5, so_luong)
        tong_tien = don_gia * so_luong_mua
        tong_so_tien += tong_tien
        kho[mat_hang] -= so_luong_mua
        hoa_don[mat_hang] = {
            'so_luong_mua': so_luong_mua,
            'don_gia': don_gia,
            'tong_tien': tong_tien
        }

for mat_hang, thong_tin_hoa_don in hoa_don.items():
    print("Thông tin hóa đơn: ")
    print(f'Mặt hàng đã mua: {mat_hang}')
    print(f"Số lượng đã mua: {thong_tin_hoa_don['so_luong_mua']}")
    print(f'Đơn giá: {thong_tin_hoa_don['don_gia']}')
    print(f'Số tiền phải trả: {thong_tin_hoa_don['tong_tien']}')
    
print(f'Tổng số tiền phải trả: {tong_so_tien}')

# in lai so luong mat hang:
for mat_hang, so_luong in kho.items():
    print(f'{mat_hang}: {so_luong}')

