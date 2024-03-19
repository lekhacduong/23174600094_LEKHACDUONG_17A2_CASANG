a,b,c = map(int,  input("Nhập số nguyên: ").split())

if a > b and a > c:
    if b > c:
        print("Số lớn thứ 2 là: ", b)
    elif c> b:
        print("Số lớn thứ 2 là: ", c)
elif b > a and b > c:
    if a > c:
        print("Số lớn thứ 2 là: ", a)
    elif c > a:
        print("Số lớn thứ 2 là: ", c)
else:
    if a > b:
        print("Số lớn thứ 2 là: ", a)
    elif b > a:
        print("Số lớn thứ 2 là: ", b)
            