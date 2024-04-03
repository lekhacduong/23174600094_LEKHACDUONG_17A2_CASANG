# a:
print("a: ")
n = 2
while n < 100:
    flag = True
    for i in range(2, int(n)):
        if n % i == 0:
            flag = False
            break
    if flag == True:
        print(n, end = " ")
    n += 1
    
print("\n")
# b:
print("b: ")

a = 2
while a ** 2 < 100:
    print(a ** 2, end = " ")
    a += 1 


print("\n")   
# c:
print("c: ")

b, c = 0, 1
while b < 1000:
    print(b, end = " ")
    b, c = c, b + c            