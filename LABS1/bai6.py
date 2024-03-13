import math

a1, a2 = eval(input("Nhập tọa độ của vecto a: "))
b1, b2 = eval(input("Nhập tọa độ của vecto b: "))

cong_2_vecto = (a1 + b1,a2 + b2)
tru_2_vecto = (a1 - b1,a2 - b2)

do_dai_vta = math.sqrt((a1 ** 2) + (a2 ** 2))
do_dai_vtb = math.sqrt((b1 ** 2) + (b2 ** 2))

tich_co_huong = (a1 * b1) + (a2 * b2)
tich_do_dai = do_dai_vta * do_dai_vtb
cos_hop_giua = tich_co_huong / tich_do_dai

print(f"Vecto a({a1,a2})")
print(f"Vecto b({b1,b2})")
print(f"Tổng 2 vecto {cong_2_vecto}")
print(f"Hiệu 2 vecto {tru_2_vecto}")
print(f"Độ dài vecto a = {do_dai_vta}")
print(f"Độ dài vecto b = {do_dai_vtb}")
print("Cos giữa 2 vecto = {:.2f} ".format(cos_hop_giua))