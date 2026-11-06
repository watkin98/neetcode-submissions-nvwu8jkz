# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            total = dfs(node.left) + dfs(node.right)
            # print(node.val)
            # print(total)
            # print()
            
            if total == node.val:
                res += 1

            return total + node.val

        tmp = dfs(root)
        return res