# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @param preorder : list of integers denoting preorder traversal of tree
# @param inorder : list of integers denoting inorder traversal of tree
# @return the root node in the tree
def buildTreeUtil(preorder, inorder, preStart, preEnd, inStart, inEnd):
    if inStart > inEnd or preStart > preEnd:
        return None
    root = TreeNode(preorder[preStart])
    for inIdx in xrange(inStart, inEnd + 1):
        if inorder[inIdx] == preorder[preStart]:
            break
    root.left = buildTreeUtil(preorder, inorder, preStart + 1, preStart + (inIdx - inStart), inStart, inIdx - 1)
    root.right = buildTreeUtil(preorder, inorder, preStart + (inIdx - inStart) + 1, preEnd, inIdx + 1, inEnd)
    return root

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    return buildTreeUtil(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

def printTree(root):
    if root:
        printTree(root.left)
        print root.val, 
        printTree(root.right)

def main():

    A = [1, 2, 3, 4, 5]
    B = [3, 4, 2, 1, 5]

    #A = [2, 1, 3]
    #B = [1, 2, 3]

    root =  buildTree(A, B)
    printTree(root)

main()