# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, prev, count):
            nonlocal res
            if not node:
                return
            # print(prev)
            # print(node.val)
            # print(count)
            # print()
            if node.val - 1 == prev:
                count += 1
            else:
                count = 1

            res = max(res, count)
            
            dfs(node.left, node.val, count)
            dfs(node.right, node.val, count)

        dfs(root, root.val - 1, 0)
        return res