chuoi = input("Nhập môt chuỗi: ").strip()
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in chuoi:
    if not i.isalnum():
        count1 += 1
    elif i.islower():
        count2 += 1
    elif i.isnumeric():
        count3 += 1
    elif i.isupper():
        count4 += 1
print("Số chữ thường trong chuỗi là:", count1)
print("Số chữ hoa trong chuỗi là:", count2)
print("Số chữ số trong chuỗi là:", count3)
print("Số chữ đặc biệt trong chuỗi là:", count4)