class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner)

    def __set__(self, instance, value):
        print(self, instance, value)

    def __delete__(self, instance):
        print(self, instance)


class Some(Descriptor):
    # x = Descriptor()
    pass


x = Some()
print(x)
x = 1
