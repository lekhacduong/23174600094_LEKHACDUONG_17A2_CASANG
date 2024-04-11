str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

gop_str = ""

min_str = 0

if len(str1) < len(str2):
    min_str = len(str1)
else:
    min_str = len(str2)

for i in range(min_str):
    gop_str += str1[i] + "-" + str2[i] + "-"
    
if len(str1) < len(str2):
    gop_str += str2[min_str :] + "-"
else:
    gop_str += str1[min_str :] + "-"

print("Chuỗi sau khi trộn là: ", gop_str.strip("-"))