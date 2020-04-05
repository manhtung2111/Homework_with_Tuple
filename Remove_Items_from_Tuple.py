tuplex = ("M", "a", "n", "h", "T", "u", "n", "g")
print(tuplex)
# remove 1 phan tu trong tuple bang cach tao ra 1 tuple moi
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
# remove 1 phan tu trong tuple bang cach chuyen tuple ve list
lst = list(tuplex)
lst.remove("T")
tuplex = tuple(lst)
print(tuplex)
