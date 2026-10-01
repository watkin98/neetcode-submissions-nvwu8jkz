# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val = 0

        def depth(node) -> int:
            nonlocal max_val
            if node is None:
                return 0

            l_depth = depth(node.left)
            r_depth = depth(node.right)
            
            max_val = max(max_val, l_depth + r_depth)

            return 1 + max(l_depth, r_depth)
            
        depth(root)
        return max_val