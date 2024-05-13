list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_number)

# 1:
so_le = list(filter(lambda x: x % 2 != 0, list_number))
print("Cac so le trong list la: ", so_le)

# 2:
so_chan = list(filter(lambda x: x % 2 == 0, list_number))
print("Cac so chan trong list la: ", so_chan)

# 3:
list_moi = list(map(lambda x: x ** 3, list_number))
print("Danh sach lap phuong cac phan tu la: ", list_moi)

# 4:
list_so_chan = list(map(lambda x: x ** 3, so_chan))
print("Danh sach lap phuong cac phan tu chan la: ", list_so_chan)

# 4:
list_so_le = list(map(lambda x: x ** 2, so_le))
print("Danh sach binh phuong cac phan tu le la: ", list_so_le)