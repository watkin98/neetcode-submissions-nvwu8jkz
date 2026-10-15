# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_seen):
            if not node:
                return 0

            if node.val >= max_seen:
                max_seen = max(max_seen, node.val)
                return 1 + dfs(node.left, max_seen) + dfs(node.right, max_seen)
            return dfs(node.left, max_seen) + dfs(node.right, max_seen)

        return dfs(root, 0)