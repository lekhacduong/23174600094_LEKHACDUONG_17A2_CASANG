# a: 
n = int(input("Nhập n: "))
list_fibonacci = [0, 1]
[list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2]) for _ in range(2, n+1)]
    
print(f"Dãy fibonacci chứa từ {n} số đầu tiên là: {list_fibonacci}")

# b:
list_so_nguyen_to = []

for i in range(100):
    if i > 1:
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            list_so_nguyen_to.append(i)

print("Danh sách các số nguyên tố nhỏ hơn 100 là: ", list_so_nguyen_to)