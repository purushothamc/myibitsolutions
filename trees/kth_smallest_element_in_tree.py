# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, A, k):
        result, output, ret_val = list(), list(), -1
        if not A and k > 0: return ret_val

        done, current, index = False, A, 0
        while not done:
            if current:
                result.append(current)
                current = current.left
            else:
                if result:
                    popped = result.pop()
                    index += 1
                    if index == k:
                        ret_val = popped.val
                        break
                    output.append(popped.val)
                    current = popped.right
                else:
                    done = True
        return ret_val
