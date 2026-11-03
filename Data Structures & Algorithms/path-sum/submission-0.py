# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False
        def dfs(node, curSum):
            nonlocal res
            if not node:
                return curSum

            left = dfs(node.left, curSum + node.val)
            right = dfs(node.right, curSum + node.val)
            
            if (left == targetSum or right == targetSum) and (not node.left and not node.right):
                res = True

        dfs(root, 0)
        return res