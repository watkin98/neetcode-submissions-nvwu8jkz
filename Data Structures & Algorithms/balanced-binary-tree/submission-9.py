# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Contract: Return subtree height or sentinel value -1 if subtree is found to be unbalanced
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            if l == -1:
                return -1
            
            r = dfs(node.right)
            if r == -1:
                return -1

            if abs(r-l) > 1:
                return -1
            else:
                return 1 + max(r, l)

        return dfs(root) != -1