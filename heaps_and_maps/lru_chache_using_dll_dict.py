from collections import OrderedDict

class DLLNode(object):
    def __init__(self, key, value):
        self.val = value
        self.next = None
        self.prev = None
        self.key = key

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, key, value):
        temp_node = DLLNode(key, value)

        if not self.head and not self.tail:
            self.head = temp_node
            self.tail = temp_node

        else:
            self.tail.next = temp_node
            temp_node.prev = self.tail
            self.tail = temp_node

        self.size += 1
        return self.tail

    def bring_to_front(self, dll_node):
        if self.size == 1:
            return

        if dll_node.prev and dll_node.next:
            prev_node = dll_node.prev
            next_node = dll_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.tail.next = dll_node
            dll_node.prev = self.tail
            dll_node.next = None
            self.tail = dll_node

        elif not dll_node.prev:
            if not dll_node.next:
                return
            temp = dll_node
            self.head = dll_node.next
            self.head.prev = None
            self.tail.next = temp
            temp.prev = self.tail
            temp.next = None
            self.tail = temp

        elif self.tail == dll_node:
            return

    def remove_least(self):
        if self.size > 0:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return temp

    def printf(self):
        temp = self.head
        while temp:
            print temp.key,
            temp = temp.next

class LRUCache(object):
    def __init__(self, size):
        #print "Creating LRU Cache of size {0}".format(size)
        self.size = size
        self.dll = DLL()
        self.mapper = OrderedDict()

    def set(self, key, value):
        if self.mapper.get(key, None):
            dll_node = self.mapper.get(key)
            dll_node.val = value
            self.dll.bring_to_front(dll_node)
        else:
            if self.dll.size < self.size:
                dll_node = self.dll.append(key, value)
                self.mapper[key] = dll_node
            else:
                #print key, value
                dll_node = self.dll.remove_least()
                self.mapper.pop(dll_node.key, None)
                dll_node = self.dll.append(key, value)
                self.mapper[key] = dll_node
        #self.dll.printf()

    def get(self, key):
        if self.mapper.get(key, None):
            self.dll.bring_to_front(self.mapper.get(key))
            print self.mapper.get(key).val
            #self.dll.printf()
        else:
            print -1

#cache = LRUCache(2)
S = "6 2 S 2 1 S 1 1 S 2 3 S 4 1 G 1 G 2"
#S = "41 5 S 7 4 G 10 S 15 4 S 11 6 S 4 14 S 11 4 G 14 S 10 7 G 15 S 13 13 G 4 G 5 S 11 8 S 14 10 G 13 S 11 15 G 9 G 14 G 2 S 9 14 S 8 8 S 5 5 S 10 15 S 7 3 S 1 6 G 15 S 3 10 G 10 G 13 S 14 12 S 11 9 S 8 15 S 1 13 G 1 G 12 G 10 G 4 G 9 G 4 G 9 G 12"

items = S.split(" ")
total = int(items[0])
size = int(items[1])
cache = LRUCache(size)
i = 2
while i < len(items):
    if items[i] == "S":
        #print "\nSetting key={0}, value={1}".format(items[i+1], items[i+2])
        cache.set(int(items[i+1]), int(items[i+2]))
        i += 3
    elif items[i] == "G":
        #print "\nGetting key={0}".format(items[i + 1])
        cache.get(int(items[i+1]))
        i += 2

"""
cache.set(1, 10)
cache.set(2, 2)
cache.get(1)
cache.set(3, 3)
cache.get(2)
cache.set(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
"""