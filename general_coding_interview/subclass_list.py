class MyList(list):
    def __init__(self, other):
        self.l = other

    @staticmethod
    def _print(self):
        print self.l


    def __repr__(self):
        print self

c = MyList([1, 2, 3])
c._print(c)