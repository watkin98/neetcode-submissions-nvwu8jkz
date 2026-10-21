# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def subTree(node, subNode):
            if not node and not subNode:
                return True
            if (node and not subNode) or (not node and subNode) or (node.val != subNode.val):
                return False
            return subTree(node.left, subNode.left) and subTree(node.right, subNode.right)
        
        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val:
                return subTree(node, subRoot)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
