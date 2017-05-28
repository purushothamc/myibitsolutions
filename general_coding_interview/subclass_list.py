import time

class MyList(list):
    def __init__(self, other):
        self.l = other

    @staticmethod
    def _print(self):
        print self.l


    def __repr__(self):
        print self


def double(f):
    def decorator(z):
        return f(z)*2
    return decorator


@double
def f(x):
    return x

print f(2)

c = MyList([1, 2, 3])
c._print(c)

class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    def __exit__(self):
        self.open_file.close()

class TimeIt():

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time

with TimeIt() as t:
    f(2)

print t.end_time