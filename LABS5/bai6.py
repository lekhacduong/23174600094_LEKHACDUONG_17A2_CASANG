chuoi = input("Nhập một chuỗi để kiểm tra: ").split()
count = 0
chuoi_dac_biet = ""

for i in chuoi:
    if not i.isalnum():
        chuoi_dac_biet += i
        count += 1
print(f"Có {count} ký tự đặc biệt xuất hiện là {chuoi_dac_biet}")

chuoi_dem = "" 
for j in chuoi_dac_biet:
    if j in chuoi_dem:
        continue
    n = chuoi_dac_biet.count(j)
    ti_le = (n / len(chuoi)) * 100
    print(f"{j} xuất hiện {n} lần trong chuỗi và chiếm {ti_le:.2f}% trong chuỗi")
    chuoi_dem += j

