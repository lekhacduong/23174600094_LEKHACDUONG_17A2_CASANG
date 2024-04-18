a = []

while True:
    x = eval(input("Nhập một số: "))
    a.append(x)
    n = input("Tiếp tục: y . Dừng lại: n   :")
    if n == 'y':
        continue
    elif n == 'n':
        break
    else:
        print("Nhập lại")

cong_sai = a[1] - a[0]
for i in range(2, len(a)):
    if a[i] - a[i - 1] == cong_sai:
        print(a)
        print("Dãy số tạo thành cấp số cộng")
        break
    else:
        print(a)
        print("Dãy số không tạo thành cấp số cộng")
        break
        
    