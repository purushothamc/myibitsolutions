from list_adt import *
def removeDuplicates(A):
    t = A
    while t and t.next:
        if t.val == t.next.val:
            x = t.next
            t.next = t.next.next
            del x
        else:
            t = t.next

def main():
    A, B = defineLists()
    A.insert_at_end(1)
    A.insert_at_end(1)
    A.insert_at_end(2)
    A.insert_at_end(3)
    A.insert_at_end(3)
    removeDuplicates(A.head)
    A.print_list()


if __name__ == '__main__':
    main()