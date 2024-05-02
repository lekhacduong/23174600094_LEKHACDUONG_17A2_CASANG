
danh_sach = {}
for i in range(10):
    ten = input("Nhap ten sinh vien thu "+ str(i+1) + ":")
    diem_thi = int(input("Nhap diem thi: "))
    danh_sach[ten] = diem_thi

danh_sach_xep_loai = {'F': 0, 'D': 0, 'C': 0, 'B': 0, 'A': 0}
for ten, diem_thi in danh_sach.items():
    if diem_thi >= 8.5:
        danh_sach_xep_loai['A'] += 1
    elif diem_thi >= 7.0 and diem_thi < 8.5:
        danh_sach_xep_loai['B'] += 1
    elif diem_thi >= 5.5 and diem_thi < 7.0:
        danh_sach_xep_loai['C'] += 1
    elif diem_thi >= 4.0 and diem_thi < 5.5:
        danh_sach_xep_loai['D'] += 1
    else:
        danh_sach_xep_loai['F'] += 1
        
print("Thong ke so luong sinh vien o moi loai hoc luc: ")
print(danh_sach_xep_loai)