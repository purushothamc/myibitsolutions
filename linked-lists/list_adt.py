class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

    def __ge__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val < other.val


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_end(self, value):
        n = ListNode(value)
        if not self.head:
            self.head = n
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = n
        self.length += 1

    def insert_at_start(self, value):
        n = ListNode(value)
        n.next = self.head
        self.head = n
        self.length += 1

    def print_list(self):
        t = self.head
        while t:
            print t.val,
            t = t.next

    def reverse(self, node):
        temp = node
        prev, next = None, None

        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev

    def reverseHelper(self, A, result):
        if not A.next:
            result = A
            return result
        result = self.reverseHelper(A.next, result)
        A.next.next = A
        A.next = None
        return result

    def reverseList(self, A):
        result = None
        return self.reverseHelper(A, result)

def defineLists():
    A = LinkedList()
    B = LinkedList()
    return A, B