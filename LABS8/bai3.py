# 1:

def cubesum(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** 3
    return sum

# 2:

def PrintArmstrong():
    for i in range(1, 10000):
        if i == cubesum(i):
            print(i, end= ' ')
    
    
def isAmrmstrong(n):
    if n == cubesum(n):
        return True
    return False   


n = int(input("Nhap n: "))
print(cubesum(n))
print('Cac so Armstrong: ')
print(PrintArmstrong())
if isAmrmstrong(n):
    print("True") 
else:
    print("False")       
