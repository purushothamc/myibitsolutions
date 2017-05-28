# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def symmetricHelper(self, left, right):
        if not left and not right:
            return 1
        if left and right and left.val == right.val:
            return self.symmetricHelper(left.left, right.right) and \
                   self.symmetricHelper(left.right, right.left)
        return 0

    def isSymmetric(self, A):
        return self.symmetricHelper(A, A)
