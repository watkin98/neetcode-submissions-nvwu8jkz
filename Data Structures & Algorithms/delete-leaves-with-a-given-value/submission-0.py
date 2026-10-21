# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node, parent):
            nonlocal root
            if not node:
                return

            dfs(node.left, node)
            dfs(node.right, node)

            if not node.left and not node.right and node.val == target:
                if not parent:
                    root = None
                elif parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
        
        dfs(root, None)
        return root 