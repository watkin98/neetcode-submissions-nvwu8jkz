# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p, q = q, p

        def dfs(node):
            if node is None:
                return root
            
            if p.val <= node.val <= q.val:
                return node
            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)
