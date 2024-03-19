print('''Chọn thể loại phim:
            1. Phim hành động
            2. Phim kinh dị
            3. Phim tình cảm
            4. Phim hài hước
            5. Phim hoạt hình
        ''')

choose = int(input("Nhập lựa chọ phim của bạn: "))
time = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ")

if choose == 1:
    if time == "sáng" or time == "trưa" or time == "chiều" or time == "tối":
        print("Phim hành động được chiếu vào mọi khung giờ trong ngày")
elif choose == 2:
    if time == "tối":
        print("Có suất chiếu phim kinh dị")
    else:
        print("Không có suất chiếu")
elif choose == 3:
    if time == "tối":
        print("Có suất chiếu phim tình cảm")
    else:
        print("Phim tình cảm chỉ được chiếu vào buổi tối")
elif choose == 4:
    if time == "sáng" or time == "trưa" or time == "chiều" or time == "tối":
        print("Phim hài hước được chiếu vào mọi khung giờ trong ngày")
else:
    if time == "tối" or time == "chiều":
        print("Không có suất chiếu")
    else:
        print("Có suất chiếu phim hoạt hình")   