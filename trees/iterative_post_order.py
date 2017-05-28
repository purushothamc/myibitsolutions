# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        output, stack = list(), list()
        if not A:
            return output

        # ----------- This solution modifies the original tree
        # we can solve using pre-order solution, pre-order: root, right, left and reverse output

        """
        stack.append(A)
        while stack:
            stack_top = stack[-1]
            if not stack_top.left and not stack_top.right:
                output.append(stack_top.val)
                stack.pop()
            else:
                if stack_top.right:
                    stack.append(stack_top.right)
                    stack_top.right = None
                if stack_top.left:
                    stack.append(stack_top.left)
                    stack_top.left = None
        return output
        """
        stack.append(A)
        while stack:
            popped = stack.pop()
            output.append(popped.val)
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
        return reversed(output)
