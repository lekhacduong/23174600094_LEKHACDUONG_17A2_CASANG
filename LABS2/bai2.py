a  = int(input("Nhập số nguyên để kiểm tra: "))

if len(str(a)) >= 4:
    print("Chữ số hàng nghìn là: ",str(a)[-4])
else:
    print("0")