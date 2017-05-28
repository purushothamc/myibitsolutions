# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @param preorder : list of integers denoting preorder traversal of tree
# @param inorder : list of integers denoting inorder traversal of tree
# @return the root node in the tree
def buildTreeUtil(postorder, inorder, postStart, postEnd, inStart, inEnd):
    if inStart > inEnd or postStart > postEnd:
        return None
    root = TreeNode(postorder[postEnd])
    for inIdx in xrange(inStart, inEnd + 1):
        if inorder[inIdx] == postorder[postEnd]:
            break
    root.left = buildTreeUtil(postorder, inorder, postStart, postStart + inIdx - (inStart + 1), inStart, inIdx - 1)
    root.right = buildTreeUtil(postorder, inorder, postStart + inIdx - inStart,  postEnd - 1, inIdx + 1, inEnd)
    return root

def buildTree(postorder, inorder):
    if not postorder or not inorder:
        return None
    return buildTreeUtil(postorder, inorder, 0, len(postorder)-1, 0, len(inorder)-1)

def printTree(root):
    if root:
        printTree(root.left)
        print root.val,
        printTree(root.right)

def main():

    #A = [1, 2, 3, 4, 5]
    #B = [3, 4, 2, 1, 5]

    #A = [2, 1, 3]
    #B = [1, 2, 3]

    B = [2, 3, 4, 5, 6, 7, 8]
    A = [2, 4, 3, 6, 8, 7, 5]

    #B = [1,2,3]
    #A = [1,3,2]

    #B = [2, 3, 4, 5, 6]
    #A = [2, 4, 3, 6, 5]

    root =  buildTree(A, B)
    printTree(root)

main()