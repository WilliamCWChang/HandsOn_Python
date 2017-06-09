class Demo:
    def __init__(self, i):
        self.i = i
        print("Demo0 -> " , end='')
        print(self.i)
    def __str__(self):
        return str(self.i)
    def hello(self):
        print("Demo0h -> ", end='')
        print("hello " + self.__str__())

class SubDemo1(Demo):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
        print("Demo1 -> ", end='')
        print(self.j)
    def __str__(self):
        print("Demo1__str__ -> ", end='')
        return super().__str__() + str(self.j)

class SubDemo2(Demo):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
        self.k = str(self.i) + str(self.j)
        print("Demo2 -> ", end='')
        print(self.k)
    def __str__(self):
        print("Demo2__str__ -> ", end='')
        return self.k


a = SubDemo1(22, 33)
b = SubDemo2(44, "55")
print('-----------------')
print(a)
print('-----------------')
a.hello()
b.hello()
