# d: y = ax + b
# d': y = cx + d
a,b = map(int, input("Nhập hệ số đường thẳng thứ nhất: ").split())
c,d = map(int, input("Nhập hệ số của đường thẳng thứ hai: ").split())

if a != 0 and c != 0:
    if a == c:
        print("Hai đường thẳng song song với nhau")
    elif a != c:
        if a * c == -1:
            print("Hai đường thẳng vuông góc với nhau")
        else:
            print("Hai đường thẳng cắt nhau")
else:
    print("Hệ số góc phải khắc 0")            
   