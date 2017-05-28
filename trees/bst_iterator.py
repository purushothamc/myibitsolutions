# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.push(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) != 0

    # @return an integer, the next smallest number
    def next(self):
        to_pop = self.stack.pop()
        if to_pop.right:
            self.push(to_pop.right)
        return to_pop.val

    def push(self, root):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
