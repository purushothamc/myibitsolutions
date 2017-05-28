from Tree import *

class BSTIterator(object):
    def __init__(self, root):
        self.st1 = list()
        self.st2 = list()
        self.p1 = root
        self.p2 = root

    def next_smallest(self):
        if self.p1:
            self.st1.append(self.p1)
            self.p1 = self.p1.left
            return self.next_smallest()
        else:
            if self.st1:
                self.p1 = self.st1.pop()
                answer = self.p1.val
                self.p1 = self.p1.right
                return answer

    def prev_largest(self):
        if self.p2:
            self.st2.append(self.p2)
            self.p2 = self.p2.right
            return self.prev_largest()
        else:
            if self.st2:
                self.p2 = self.st2.pop()
                answer = self.p2.val
                self.p2 = self.p2.left
                return answer

def t2Sum(self, root, target):
    bst = BST(root)
    x1 = bst.next_smallest()
    x2 = bst.prev_largest()
    while x1 < x2:
        if x1 + x2 == target: return 1
        if x1 + x2 < target:
            x1 = bst.next_smallest()
        else:
            x2 = bst.prev_largest()
    return 0


def t2Sum(root, target):
    bst = BSTIterator(root)
    x1 = bst.next_smallest()
    x2 = bst.prev_largest()
    while x1 < x2:
        if x1 + x2 == target: return 1
        if x1 + x2 < target:
            x1 = bst.next_smallest()
        else:
            x2 = bst.prev_largest()
    return 0

print t2Sum(BinaryTree([12, 4, 19, -1, 5, -1, -1]).root, 17)



def t2SumAnotherSolution(self, root, target):
    result = 0
    if not root:
        return result
    leftStack, rightStack = list(), list()
    A, B = root, root

    while leftStack or rightStack or A or B:
        if A or B:
            if A:
                leftStack.append(A)
                A = A.left
            if B:
                rightStack.append(B)
                B = B.right
        else:
            if leftStack[-1].val >= rightStack[-1].val:
                return 0

            curSum = leftStack[-1].val + rightStack[-1].val
            if curSum > target:
                popped = rightStack.pop()
                B = popped.left

            elif curSum < target:
                popped = leftStack.pop()
                A = popped.right

            else:
                result = 1
                break
    return result