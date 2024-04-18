# 6.1

m = int(input("Nhập số hàng của ma trận A: "))
n = int(input("Nhập số cột của ma trận A: "))

matrix_A = []
for i in range(m):
    row1 = []
    for j in range(n):
        gia_tri1 = int(input(f"Nhập phần tử hàng {i+1} cột {j+1}: "))
        row1.append(gia_tri1)
    matrix_A.append(row1)

print("Ma trận A: ")
for row1 in matrix_A:
    print(" ".join(map(str, row1)))


sum = 0
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[i])):
        sum += matrix_A[i][j]
print("Tổng tất cả các phần tử trong ma trận A là: ", sum)


# ma tran B
matrix_B = []
a = int(input("Nhập số hàng ma trận B: "))
b = int(input("Nhập số cột ma trận B: "))

for i in range(a):
    row2 = []
    for j in range(b):
        gia_tri2 = int(input(f"Nhập phần tử hàng {i+1} cột {j+1}: "))
        row2.append(gia_tri2)
    matrix_B.append(row2)

print("Ma trận B: ")
for row2 in matrix_B:
    print(" ".join(map(str, row2)))

# nhân 2 ma trận:
if n != a:
    print("Không thể nhân 2 ma trận với kích thước không phù hợp")
else:
    matrix_tich = []
    for i in range(m):
        row3 = []
        for j in range(b):
            row3.append(0)
        matrix_tich.append(row3)
        
    for i in range(m):
        for j in range(b):
            for l in range(n):
                matrix_tich[i][j] += matrix_A[i][l] * matrix_B[l][j]
                
    print("Tích của 2 ma trận là: ")
    for row3 in matrix_tich:
        print(" ".join(map(str, row3)))


# ma tran chuyen vi
matrix_chuyen_vi = []
for i in range(n):
    row4 = []
    for j in range(m):
        row4.append(matrix_A[j][i])
    matrix_chuyen_vi.append(row4)
    
print("Ma trận chuyển vị của ma trận A là: ")
for row4 in matrix_chuyen_vi:
    print(" ".join(map(str, row4)))
    
    