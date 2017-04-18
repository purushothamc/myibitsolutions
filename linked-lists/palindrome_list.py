from list_adt import *

left = None

def isPalHelper(A):
    global left
    if not A or not left:
        return True
    result = isPalHelper(A.next)
    if not result:
        return False
    if left.val == A.val:
        left = left.next
        return True
    else:
        return False

def isPalindrome(A):
    global left
    left = A
    return isPalHelper(A)

def main():
    A, B = defineLists()
    for i in xrange(1, 3):
        A.insert_at_end(i)
    for i in xrange(1, 0, -1):
        A.insert_at_end(i)
    A.print_list()
    print isPalindrome(A.head)

if __name__ == '__main__':
    main()
