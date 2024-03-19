a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b :"))

print(f"Phương trình bậc nhất {a}x + {b} = 0")

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Vô lý, phương trình vô nghiệm")
elif b == 0:
    print("Phương trình có nghiệm x = 0")
else:
    print("Phương trình có nghiệm: x =", -b/a)
        