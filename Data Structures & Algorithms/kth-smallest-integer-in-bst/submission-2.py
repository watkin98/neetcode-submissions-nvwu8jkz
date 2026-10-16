# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        isFound = False
        res = None

        def dfs(node, isFound):
            nonlocal res
            nonlocal count
            if not node or isFound:
                return None

            dfs(node.left, isFound)
            count += 1
            if count == k:
                res = node.val
                return 
            dfs(node.right, isFound)

        dfs(root, isFound)
        return res
