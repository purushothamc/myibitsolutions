# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def findNodeWithData(self, A, B):
        if not A: return None
        if A.val == B: return A
        if B < A.val: return self.findNodeWithData(A.left, B)
        elif B > A.val: return self.findNodeWithData(A.right, B)

    def findMin(self, A):
        if not A: return None
        while A.left:
            A = A.left
        return A

    def getSuccessor(self, A, B):
        if not A:
            return None
        current = self.findNodeWithData(A, B)
        if not current: return None
        if current.right:
            return self.findMin(A)
        else:
            successor = None
            ancestor = A
            while current != ancestor:
                if current.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor
