class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None


def copyRandomList(head):
    mapper = dict()
    c, copy = head, None
    while c:
        copy = RandomListNode(c.label)
        mapper[c] = copy
        c = c.next
    c = head
    while c:
        copy = mapper[c]
        if not c.next:
            copy.next = None
        else:
            copy.next = mapper[c.next]
        if not c.random:
            copy.random = None
        else:
            copy.random = mapper[c.random]
        c = c.next
    return mapper[head]