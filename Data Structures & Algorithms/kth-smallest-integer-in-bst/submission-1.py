# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = []
        isFound = False

        def dfs(node):
            nonlocal seen
            nonlocal isFound
            if not node or isFound:
                return

            dfs(node.left)
            seen.append(node.val)
            if len(seen) == k:
                isFound = True
                return
            dfs(node.right)

        dfs(root)
        return seen[k-1]