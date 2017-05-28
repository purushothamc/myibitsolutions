# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers

    def vertical_traversal_helper(self, A, v_map, count):
        if not A:
            return
        queue = deque()
        queue.append((A, count))
        while queue:
            first = queue.popleft()
            count = first[1]
            v_map[count].append(first[0].val)
            if first[0].left:
                queue.append((first[0].left, count - 1))
            if first[0].right:
                queue.append((first[0].right, count + 1))

    def verticalOrderTraversal(self, A):
        output = list()
        if not A:
            return output
        vertical_map = defaultdict(list)
        self.vertical_traversal_helper(A, vertical_map, 0)

        for key in sorted(vertical_map.keys()):
            output.append(vertical_map[key])
        return output
