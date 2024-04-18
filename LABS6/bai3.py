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

min = 0
max = 0

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    else:
        min = a[i]


print("List a: ", a)
print("Phần tử lớn nhất trong danh sách là: ", max)
print("Phần từ nhỏ nhất trong danh sách là: ", min)
    