# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSumHelper(self, root, sum1, path, result):
        if not root:
            return
        if not root.left and not root.right and sum1 - root.val == 0:
            path.append(root.val)
            temp = [y for y in path]
            result.append(temp)
            path.pop()
            return

        path.append(root.val)
        self.pathSumHelper(root.left, sum1 - root.val, path, result)
        self.pathSumHelper(root.right, sum1 - root.val, path, result)
        path.pop()

    def pathSum(self, root, sum1):
        result, path = list(), list()
        if not root:
            return result
        self.pathSumHelper(root, sum1, path, result)
        return result
