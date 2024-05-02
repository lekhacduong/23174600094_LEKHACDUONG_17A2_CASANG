le_khac_duong = {}
n = int(input("Nhap n: "))
for x in range(1, n+1):
    le_khac_duong[x] = x ** 3
print(f"Tu dien co key la x va value la x^3 co do dai bang {n} la: \n", le_khac_duong)