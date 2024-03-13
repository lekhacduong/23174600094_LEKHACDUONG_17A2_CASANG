tien_ban_dau = 10000
lai_suat = 0.06
# tien lai sau 5 nam
amount_after_5_years = tien_ban_dau * ((1 + lai_suat) ** 5)
# tien lai sau 10 nam
amount_after_10_years = tien_ban_dau * ((1 + lai_suat) ** 10)
# tinh ty le tang trương
growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years
# in ra man hinh
print("Số tiền có sau 5 năm là: {:.2f}".format(amount_after_5_years))
print("Số tiền có sau 10 năm là: {:.2f}".format(amount_after_10_years))
print("Tỉ lệ tăng trưởng số tiền sau 10 năm so với 5 năm là: {:.2f}".format(growth_rate))
