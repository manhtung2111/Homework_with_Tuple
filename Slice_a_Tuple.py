tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex)  # in ra tuple
# in ra elements o vi tri 3 va 4 trong tuple
_slice = tuplex[3:5]
print(_slice)
# in ra elements tu vi tri 0 -> 5 trong tuple
_slice = tuplex[:6]
print(_slice)
# in ra tat ca cac elements
_slice = tuplex[:]
print(_slice)
# gan 1 string thanh 1 tuple roi in ra duoi dang tuple
tupley = tuple("HELLO WORLD")
print(tupley)
# tu element 2->8 trong tuple in ra cac elements cach nhau 2 vi tri
_slice = tupley[2:9:2]
print(_slice)
# in ra cac elements cach nhau 2 vi tri trong tuple
_slice = tupley[::2]
print(_slice)
