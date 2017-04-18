from list_adt import *

def swapNodes(A):
    t = A
    while t and t.next:
        a = t.next


def main():
    A, B = defineLists()
    for i in xrange(1, 10):
        A.insert_at_end(i)
    swapNodes(A.head)
    A.print_list()

if __name__ == '__main__':
    main()