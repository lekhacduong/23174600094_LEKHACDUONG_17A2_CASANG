import math
x = float(input("Nhập x: "))
z = float(input("Nhập z: "))

f = (((x ** 2) * (math.sin(z) + math.sqrt(abs(x)))) / ((math.log(z)) + pow(math.e, x-1))) + (math.atan(x * z))

print("f(x,z) = {:.2f}".format(f))


