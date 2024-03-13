canh_day = int(input("Nhập cạnh đáy: "))
chieu_cao = int(input("Nhập chiều cao: "))
dien_tich_day = canh_day ** 2
chu_vi_day =  canh_day * 4
dien_tich_xung_quanh = chu_vi_day * (chieu_cao / 2)
dien_tch_toan_phan = dien_tich_xung_quanh + dien_tich_day
the_tich = 1/3 * dien_tich_day * chieu_cao
# in
print("Diện tích xung quanh hình chóp tứ giác đều có cạnh đáy {} và chiều cao {} là: {:.2f}".format(canh_day,chieu_cao,dien_tich_xung_quanh))
print("Diện tích toàn phần hình chóp tứ giác đều có cạnh đáy {} và chiều cao {} là: {:.2f}".format(canh_day,chieu_cao,dien_tch_toan_phan))
print("Thể tích hình chóp tứ giác đều có cạnh đáy {} và chiều cao {} là: {:.2f}".format(canh_day,chieu_cao,the_tich))
