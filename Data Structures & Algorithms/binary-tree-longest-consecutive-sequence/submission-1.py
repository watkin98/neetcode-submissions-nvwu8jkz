# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, prev, length):
            nonlocal res
            if not node:
                return

            if node.val-1 == prev:
                length += 1
            else:
                length = 1

            res = max(res, length)

            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)

        dfs(root, None, 0)
        return res