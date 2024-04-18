a = []
list_chan = []
list_le = []
while True:
    x = int(input("Nhập số nguyên: "))
    a.append(x)
    n = input("Tiếp tục: y . Dừng lại: n   :")
    if n == 'y':
        continue
    elif n == 'n':
        break
    else:
        print("Nhập lại")

for i in a:
    if i % 2 == 0:
        list_chan.append(i)
    else:
        list_le.append(i)

tinh_tong_chan = sum(list_chan)
tinh_tong_le = sum(list_le)

print("Tổng các số chẵn trong mảng là: ", tinh_tong_chan)
print("Tổng các số lẻ trong mảng là: ", tinh_tong_le)


