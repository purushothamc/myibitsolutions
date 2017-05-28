class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# This tree builds on input like this
# it takes list of values, where node's value represented by
# current index value and left, right nodes are represented by
# index*2, index*2+1 values of input list.
# leaf nodes are represented as -1s
class BinaryTree(object):
    def __init__(self, input_list):
        self.root = None
        self.root = self._build_tree(input_list, 0, self.root)

    def _build_tree(self, input_list, index, root):
        if not input_list or index > len(input_list) or input_list[index] == -1:
            root = None
        else:
            root = TreeNode(input_list[index])
            root.left = self._build_tree(input_list, 2*index + 1, root.left)
            root.right = self._build_tree(input_list, 2*index + 2, root.right)
        return root

    def inorder_traverse(self, root):
        if root:
            self.inorder_traverse(root.left)
            print root.val,
            self.inorder_traverse(root.right)

    def preorder_traverse(self, root):
        if root:
            print root.val,
            self.preorder_traverse(root.left)
            self.preorder_traverse(root.right)

    def postorder_traverse(self, root):
        if root:
            self.postorder_traverse(root.left)
            self.postorder_traverse(root.right)
            print root.val,

#bst = BinaryTree([2, 4, 19, -1, 5, -1, -1])
#bst.preorder_traverse(bst.root)