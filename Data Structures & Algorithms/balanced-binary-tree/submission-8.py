# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper contract: pass in the node and return the depth of the 
        #                  subtree on that side. If subtree is found to 
        #                  be unbalanced, short-circuit and return -1.
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)

            if right == -1 or abs(right - left) > 1:
                return -1
            
            return 1 + max(left, right)
                    
        return dfs(root) != -1