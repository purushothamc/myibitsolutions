# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque

class Solution:
    # @param root, a tree node
    # @return nothing
    def connectV1(self, root):
        q1, q2 = deque(), deque()
        q1.append(root)

        while q1:
            popped = q1.popleft()
            if not q1:
                popped.next = None
            else:
                popped.next = q1[0]
            if popped.left:
                q2.append(popped.left)
            if popped.right:
                q2.append(popped.right)
            if not q1:
                q1 = q2
                q2 = deque()
        return root

    def connect(self, root):
        # Works only for FULL binary trees.
        p = root
        p.next = None
        while p:
            q = p
            while q:
                if q.left:
                    q.left.next = q.right
                if q.right:
                    q.right.next = q.next.left if q.next else None
                q = q.next
            if p.left:
                p = p.left
            else:
                break