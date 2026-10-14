# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = []
        res = None

        def dfs(node):
            nonlocal seen
            nonlocal res
            if not node:
                return

            dfs(node.left)
            seen.append(node.val)
            if len(seen) == k:
                res = seen[-1]
                return
            dfs(node.right)

        dfs(root)
        return res