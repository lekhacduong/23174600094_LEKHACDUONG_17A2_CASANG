n = int(input("Nhập kích thước của ma trận vuông: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        gia_tri = int(input(f"Nhập phẩn thử hàng {i+1} cột {j+1}"))
        row.append(gia_tri)
    matrix.append(row)

print("Ma trận vuông đã nhập là: ")
for row in matrix:
    print(" ".join(map(str, row)))
    

# mtr don vi
matrix_don_vi = []
for i in range(n):
    row1 = []
    for j in range(n):
        if i == j:
            gia_tri2 = 1
            row1.append(gia_tri2)
        else:
            gia_tri2 = 0
            row.append(gia_tri2)
    matrix_don_vi.append(row1)

# tim mtr nghịch đảo
for j in range(n):
    for i in range(n):
        matrix2 = matrix[i][j] + matrix_don_vi[i]

for i in range(n):
    if matrix2[i][i] == 0:
        print("Không tìm được ma trận nghịch đảo")
        break