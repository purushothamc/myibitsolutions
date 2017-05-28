# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBSTUtil(self, A, start, end):
        if start > end:
            return None
        midIndex = start + ((end - start) / 2)
        root = TreeNode(A[midIndex])
        root.left = self.sortedArrayToBSTUtil(A, start, midIndex-1)
        root.right = self.sortedArrayToBSTUtil(A, midIndex+1, end)
        return root

    def sortedArrayToBST(self, A):
        if not A:
            return None
        start, end = 0, len(A) - 1
        return self.sortedArrayToBSTUtil(A, start, end)
