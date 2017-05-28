def bstUtil(root):
    if not root:
        return root

    if root.left:
        left = bstUtil(root.left)
        while left.right is not None:
            left = left.right
        left.right = root
        root.left = left

    if root.right:
        right = bstUtil(root.right)
        while right.left is not None:
            right = right.left
        right.left = root
        root.right = right
    return root

def bstToDLL(root):
    if not root:
        return
    bstUtil(root)