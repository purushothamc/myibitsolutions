# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTreeHelper(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

    def invertTree(self, root):
        self.invertTreeHelper(root)
        return root

    def invertTreeAnotherSolution(self, root):
        if not root:
            return root
        root.left = self.invertTreeAnotherSolution(root.left)
        root.right = self.invertTreeAnotherSolution(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root