# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Contract: recursive function receives a node and returns a set of node values seen
        # Base Case: when node is None or found is True, return an empty set
        res = None
        found = False
        def dfs(node):
            nonlocal found
            nonlocal res
            if not node or found:
                return set()

            left = dfs(node.left)
            if found:
                return set()
            right = dfs(node.right)
            if found:
                return set()

            seen = set()
            for item in left:
                seen.add(item)
            for item in right:
                seen.add(item)
            seen.add(node.val)
            
            if q.val in seen and p.val in seen:
                res = node
                found = True
                return set()
            else:
                return seen

        dfs(root)
        return res



