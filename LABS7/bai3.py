str = 'I am an avid reader. Book reading is my hobby. The book I like the most is a story book by Munsi Premchand. He is a well known name in Hindi literature. All his stories are close to the reality of Indian society. His characters are simple and from real life. He raised many social issues in his stories. He had a good understanding of his time. His stories are mirror of society. That’s why he is popular among common mass.'
a = str.lower().split()

so_luong_tu = {}

for i in a:
    if i in so_luong_tu:
        so_luong_tu[i] += 1
    else:
        so_luong_tu[i] = 1
# in tu so luong nhieu nhat:
tu_xuat_hien_nhieu_nhat = max(so_luong_tu.values())
tu_xuat_hien_it_nhat = min(so_luong_tu.values())


print("Đếm số lượng: \n", so_luong_tu)

for i in [i for i, j in so_luong_tu.items() if j == tu_xuat_hien_nhieu_nhat]:
    print("Từ xuất hiện nhiều nhất: \n", i)

for i in [i for i, j in so_luong_tu.items() if j == tu_xuat_hien_it_nhat]:
    print("Từ xuất hiện ít nhất: \n", i)

