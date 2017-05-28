# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def findMax(self, X):
        if len(X) == 1:
            return 0
        curMax, fIndex = X[0], 0
        for index in xrange(len(X)):
            if curMax < X[index]:
                curMax = X[index]
                fIndex = index
        return fIndex

    def buildTree(self, A):
        if not A:
            return None
        maxValIndex = self.findMax(A)
        root = TreeNode(A[maxValIndex])
        root.left = self.buildTree(A[:maxValIndex])
        root.right = self.buildTree(A[maxValIndex + 1:])
        return root
