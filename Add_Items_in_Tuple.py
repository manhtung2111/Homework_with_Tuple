tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# cong them phan tu 12 tuy nhien 12 phai duoc khai bao o dang tuple
tuplex = tuplex + (12,)
print(tuplex)
# cong them phan tu 15,20 vao vi tri dang sau phan tu thu 2
tuplex = tuplex[:2] + (15, 20) + tuplex[2:]
print(tuplex)
# them 1 phan tu bang cach chuyen ve list va su dung append()
lst = list(tuplex)
lst.append(21)
tuplex = tuple(lst)
print(tuplex)
