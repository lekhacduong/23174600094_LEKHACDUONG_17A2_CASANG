def sumPdivisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum 

n = int(input("Nhap n: "))
print(f'Tong cac uoc so chinh cua {n} la: {sumPdivisors(n)}')




