class MyClass(object):
    def __init__(self, x):
        self.y = x
    @classmethod
    def simple(cls, arg1):
        print arg1

class Derived(MyClass):
    def __init__(self,x ):
        super(Derived, self).__init__(x)
    @classmethod
    def simple(cls, arg1):
        print arg1

d = Derived(2)
print d.y