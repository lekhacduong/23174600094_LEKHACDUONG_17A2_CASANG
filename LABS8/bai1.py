def so_nguyen_to(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
so_nguyen_to_sinh_doi = []
for i in range(3, 1000, 2):
    if so_nguyen_to(i):
        so_nguyen_to_sinh_doi.append(i)
        so_nguyen_to_sinh_doi.append(i + 2)
    

for j in so_nguyen_to_sinh_doi:
    print(j, end= ' ')