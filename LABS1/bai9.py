m1, m2 = eval(input("Nhập tọa độ đỉnh M: "))
n1, n2 = eval(input("Nhập tọa độ đỉnh N: "))
p1, p2 = eval(input("Nhập tọa độ đỉnh P: "))
q1, q2 = eval(input("Nhập tọa độ đình Q: "))

trung_diem_MN = ((m1 + n1) / 2,(m2 + n2) / 2)
trung_diem_NP = ((n1 + p1) / 2,(n2 + p2) / 2)
trung_diem_PQ = ((p1 + q1) / 2,(p2 + q2) / 2)
trung_diem_QM = ((q1 + m1) / 2,(q2 + m2) / 2)

print("Trung điểm cạnh MN là:",trung_diem_MN)
print("Trung điểm cạnh NP là:",trung_diem_NP)
print("Trung điểm cạnh PQ là:",trung_diem_PQ)
print("Trung điểm cạnh QM là:",trung_diem_QM)
