import Queue as Q


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            temp = ListNode(value)
            self.tail.next = temp
            self.tail = temp

class PQElement(object):
    def __init__(self, val, array_number, index_in_array):
        self.number = val
        self.array_index = array_number
        self.number_index = index_in_array

    def __cmp__(self, other):
        return self.number > other.number

class PQListElement(object):
    def __init__(self, val, array_number, array_head):
        self.number = val
        self.array_index = array_number
        self.head = array_head

    def __cmp__(self, other):
        return self.number > other.number


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def mergeK(self, A):
        result = list()
        q = Q.PriorityQueue()

        if not A: return result

        for index, lst in enumerate(A):
            element = PQElement(lst[0], index, 0)
            q.put(element)

        while not q.empty():
            element = q.get()
            result.append(element.number)
            if element.number_index + 1 < len(A[element.array_index]):
                next_element = PQElement(A[element.array_index][element.number_index + 1],
                                         element.array_index, element.number_index + 1)
                q.put(next_element)
        print result

    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        q = Q.PriorityQueue()
        L = LinkedList()

        for index, lst in enumerate(A):
            element = PQListElement(lst.val, index, lst)
            q.put(element)

        while not q.empty():
            element = q.get()
            # result.append(element.number)
            L.append(element.number)

            if element.head.next:
                next_element = PQListElement(element.head.next.val,
                                             element.array_index, element.head.next)
                q.put(next_element)

        return L.head


A = [[5, 6], [1, 3], [2, 4]]
C = Solution()
C.mergeK(A)