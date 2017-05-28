# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        if not A:
            return list()
        output, stack = list(), list()
        stack.append(A)
        while stack:
            popped = stack.pop()
            output.append(popped.val)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)
        return output
