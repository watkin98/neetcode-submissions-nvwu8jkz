# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def dfs(node, l_bound, r_bound):
            nonlocal isValid
            if not node or not isValid:
                return

            if not l_bound < node.val < r_bound:
                isValid = False
                return

            dfs(node.left, l_bound, node.val)
            dfs(node.right, node.val, r_bound)

        dfs(root, float('-inf'), float('inf'))
        return isValid 