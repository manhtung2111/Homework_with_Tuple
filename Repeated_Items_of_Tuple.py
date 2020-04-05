class repeat_tuple:
    def __init__(self, tple):  # khai bao class co thuoc tinh tple
        self.tple = tple

    def find_repeat(self, n):  # khai bao ham co thuoc tinh n
        count = self.tple.count(n)  # dem co lan xuat hien cua phan tu n
        print(count)


tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
test = repeat_tuple(tuplex) # khai bao object test
test.find_repeat(4)
