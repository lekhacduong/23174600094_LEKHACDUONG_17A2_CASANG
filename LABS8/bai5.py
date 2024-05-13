def sumPdivisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum 


def so_amicable(a, b):
    if sumPdivisors(a) == b and sumPdivisors(b) == a:
        return True
    return False



a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))

if so_amicable(a, b):
    print("2 so la so amicable")
else:
    print("2 so khong phai la so amicalbe")