# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        output, temp = list(), list()
        if not A: return output
        q1, q2 = list(), list()
        q1.append(A)
        while q1 or q2:
            temp = list()
            while q1:
                popped = q1.pop()
                temp.append(popped.val)
                if popped.left:
                    q2.append(popped.left)
                if popped.right:
                    q2.append(popped.right)
            if temp:
                output.append([y for y in temp])
            temp = list()
            while q2:
                popped = q2.pop()
                temp.append(popped.val)
                if popped.right:
                    q1.append(popped.right)
                if popped.left:
                    q1.append(popped.left)
            if temp:
                output.append([y for y in temp])
        return output
