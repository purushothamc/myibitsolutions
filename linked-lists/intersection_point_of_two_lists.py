from list_adt import *

def findInterSection(A, B):
    c1, c2 = 0, 0
    t1, t2 = A, B
    while t1:
        c1 += 1
        t1 = t1.next
    while t2:
        c2 += 1
        t2 = t2.next
    idx, t1, t2 = 0, A, B
    if c1 > c2:
        while idx < (c1 - c2) and t1:
            t1 = t1.next
            idx += 1
    else:
        while idx < (c2 - c1) and t2:
            t2 = t2.next
            idx += 1
    while t1 and t2:
        if t1 == t2:
            return t1
        else:
            t1 = t1.next
            t2 = t2.next
    return None

def main():
    A, B = defineLists()
    print findInterSection(A.head, B.head).val

if __name__ == '__main__':
    main()