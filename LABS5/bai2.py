str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
min_chuoi = 0
chuoi_con = ""

if len(str1) < len(str2):
    min_chuoi = len(str1)
elif len(str2) < len(str1):
    min_chuoi = len(str2)
    
for i in range(min_chuoi, 0, -1):
    for j in range(len(str1) - i + 1):
        chuoi = str1[j:j + i]
        if chuoi in str2:
            chuoi_con = chuoi
    if chuoi_con:
        break

if chuoi_con:
    print("Chuỗi ký tự con chung có độ dài ngắn nhất là: ", chuoi_con)