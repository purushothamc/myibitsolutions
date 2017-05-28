# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def pathSumHelper(self, root, sum1, path, result):
        if not root:
            if sum != 0: return False
            if sum == 0: return True

        if not root.left and not root.right and sum1 - root.val == 0:
            path.append(root.val)
            temp = [y for y in path]
            result.append(temp)
            path.pop()
            return True

        path.append(root.val)
        ret_val = self.pathSumHelper(root.left, sum1-root.val, path, result)
        if ret_val: return ret_val
        ret_val = self.pathSumHelper(root.right, sum1-root.val, path, result)
        if ret_val: return ret_val
        path.pop()
        return ret_val

    def hasPathSum(self, root, sum1):
        result, path = list(), list()
        if not root:
            if sum != 0: return False
            if sum == 0: return True
        retVal = self.pathSumHelper(root, sum1, path, result)
        return retVal

    def hasPathSumAnotherSolution(self, A, B):
        if not A: return False
        if not A.left and not A.right: return B == A.val
        remainingSum = B - A.val
        return self.hasPathSum(A.left, remainingSum) or self.hasPathSum(A.right, remainingSum)