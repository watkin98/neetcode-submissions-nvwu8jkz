# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isDuplicate(node, subNode):
            if node is None and subNode is None:
                return True
            elif node and subNode and node.val == subNode.val:
                return isDuplicate(node.left, subNode.left) and isDuplicate(node.right, subNode.right)
            else:
                return False

        def dfs_root_search(node):
            if node is None:
                return False

            if node.val == subRoot.val and isDuplicate(node, subRoot):
                return True

            return dfs_root_search(node.left) or dfs_root_search(node.right)

        return dfs_root_search(root)