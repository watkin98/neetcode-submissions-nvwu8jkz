# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            l_edges = dfs(node.left)
            r_edges = dfs(node.right)
            res = max(res, l_edges + r_edges)

            return max(l_edges, r_edges) + 1

        dfs(root)
        return res