# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def bstHeight(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        height = max(self.bstHeight(root.left), self.bstHeight(root.right)) + 1
        return height

    def isBalanced(self, A):
        if not A or (not A.left and not A.right):
            return 1
        lh = self.bstHeight(A.left)
        rh = self.bstHeight(A.right)
        if abs(lh - rh) > 1:
            return 0
        return abs(lh - rh) <= 1 and self.isBalanced(A.left) and self.isBalanced(A.right)