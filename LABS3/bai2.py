# a:
tonga = 0

for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tonga += i
print("Tổng các số chia hết cho 7 và không chia hết cho 5 trong khoảng 2000 đến 4000 là: ",tonga)
    
# b:
tongb = 0

for j in range(500, 1001):
    if j % 4 == 0 and j % 6 != 0:
        tongb += j
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoang 500 đến 1000 là: ",tongb)        