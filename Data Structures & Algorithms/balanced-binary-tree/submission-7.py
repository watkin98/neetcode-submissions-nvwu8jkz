# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        # helper contract: pass in the node and return the depth of the 
        #                  subtree on that side. Use a shared variable to
        #                  track the truth of the balanced property (T or F)
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if res and abs(r-l) <= 1:
                return 1 + max(l, r)
            else:
                res = False

        dfs(root)
        return res