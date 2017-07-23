# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def _helper(self, root):
        if root:
            self._helper(root.left)
            if self.prev and self.prev.val >= root.val:
                if not self.mapper['first']:
                    self.mapper['first'] = self.prev
                    self.mapper['middle'] = root
                else:
                    self.mapper['last'] = root
            self.prev = root
            self._helper(root.right)

    def recoverTree(self, root):
        self.mapper = dict()
        self.mapper['first'], self.mapper['middle'], self.mapper['last'] = None, None, None
        self.prev = None

        self._helper(root)

        if self.mapper['first'] and self.mapper['last']:
            return sorted([self.mapper['first'].val, self.mapper['last'].val])
        elif self.mapper['first'] and self.mapper['middle']:
            return sorted([self.mapper['first'].val, self.mapper['middle'].val])
