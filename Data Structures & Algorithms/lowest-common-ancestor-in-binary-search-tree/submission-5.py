# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            q, p = p, q

        p, q = p.val, q.val

        def dfs(node):
            if not node:
                return root

            if p <= node.val <= q:
                return node
            elif p < q < node.val:
                return dfs(node.left)
            else:   # node.val > q > p
                return dfs(node.right)

        return dfs(root)

            