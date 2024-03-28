import math
n = int(input("NHập vào một số nguyên dương: "))
s1 = 0
s2 = 0
s3 = 0
s4 = 0
if n <= 0:
    print("Yêu cầu nhập lại")
else:
    for i in range(1,n+1):
       # 1:
       s1 += i
       # 2:
       s2 += 1 / i
       # 3:
       s3 += 1 / math.sqrt(2 * i)
       # s4:
       s4 += (-1) ** (i - 1) / (2 * i - 1)
       
print("S1 = ",s1)
print("S2 = ",s2)
print("S3 = ",s3)
print("S4 = ",s4)