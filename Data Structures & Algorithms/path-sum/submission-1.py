# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0

        def dfs(node, subtotal):
            if not node:
                return False

            subtotal += node.val

            if not node.left and not node.right and subtotal == targetSum:
                return True
            else:
                return dfs(node.left, subtotal) or dfs(node.right, subtotal)

        return dfs(root, 0)