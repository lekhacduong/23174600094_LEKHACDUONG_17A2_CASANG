chuoi1 = input("Nhập một chuỗi để kiểm tra: ")
chuoi2 = ""

for i in chuoi1:
    if i.isnumeric():
        chuoi2 += i
print("Chuỗi sau khi xóa các kí tự không phải số là: ", chuoi2)

chuoi_so = int(chuoi2)
tong = 0
for i in range(1, chuoi_so):
    if chuoi_so % i == 0:
        tong += i
if tong == chuoi_so:
    print("Chuỗi số là số hoàn hảo")
else:
    print("Chuỗi số không phải số hoàn haỏ")
    
    