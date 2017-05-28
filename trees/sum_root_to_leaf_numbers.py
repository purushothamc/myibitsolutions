# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbersHelper(self, root, output, currentPathSum):
        if not root:
            return 0
        if not root.left and not root.right:
            currentPathSum *= 10
            currentPathSum += root.val
            output.append(currentPathSum)
            return
        currentPathSum *= 10
        currentPathSum = currentPathSum + root.val
        self.sumNumbersHelper(root.left, output, currentPathSum)
        self.sumNumbersHelper(root.right, output, currentPathSum)

    def sumNumbers(self, A):
        output, path = list(), list()
        if not A:
            return 0
        self.sumNumbersHelper(A, output, 0)
        return sum(output) % 1003
