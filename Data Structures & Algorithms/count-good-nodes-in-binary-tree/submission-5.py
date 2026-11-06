# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, seen):
            nonlocal res
            if not node:
                return

            if node.val >= seen:
                res += 1
                seen = node.val

            dfs(node.left, seen)
            dfs(node.right, seen)

        dfs(root, float('-inf'))
        return res
            
    def countQualifyingNodes(root) -> int:
        res = 0

        def dfs(node, max_ancestor):
            nonlocal res
            if not node:
                return float('-inf')

            new_max_ancestor = max(max_ancestor, node.val)
            max_decendent = max(dfs(node.left, new_max_ancestor), dfs(node.right, new_max_ancestor))

            if max_ancestor < node.val > max_decendent:
                res += 1
                return node.val
            return max_decendent if max_decendent != float('-inf') else node.val

        dfs(root, float('-inf'))
        return res
            
        