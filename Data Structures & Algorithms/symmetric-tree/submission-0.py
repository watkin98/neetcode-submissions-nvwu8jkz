# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Contract: takes in symmentrically corresponding left and right nodes and returns
        #           a boolean for whether left and right subtrees are symmetrical
        def dfs(left, right) -> bool:
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)