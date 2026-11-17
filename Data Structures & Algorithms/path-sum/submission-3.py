# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # Contract: receives a reference to a node and current sum along the path.
        #           Returns True if the program is at a leaf node and the current sum
        #           plus the leaf equals the target sum.
        def dfs(node, curSum):
            if not node:
                return False
            
            left = dfs(node.left, curSum + node.val)
            right = dfs(node.right, curSum + node.val)

            if node.left is None and node.right is None and curSum + node.val == targetSum:
                return True

            if left:
                return left
            if right:
                return right

            return False

        return dfs(root, 0)
