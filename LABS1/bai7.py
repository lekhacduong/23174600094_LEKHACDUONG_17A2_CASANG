print("Nhaaph hpt 2 ẩn: ")
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))

a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))

x = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
y = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)

print("Nghiệm của hpt trên là: ")
print("X = {:.2f}".format(x))
print("Y = {:.2f}".format(y))
