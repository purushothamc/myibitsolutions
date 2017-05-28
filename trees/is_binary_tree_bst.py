# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBstUtil(self, A, minVal, maxVal):
        if not A:
            return True
        if A.val >= minVal and A.val < maxVal and \
            self.isBstUtil(A.left, minVal, A.val) and \
            self.isBstUtil(A.right, A.val, maxVal):
            return True
        return False

    def isValidBST(self, A):
        return self.isBstUtil(A, -1*sys.maxint, sys.maxint)
