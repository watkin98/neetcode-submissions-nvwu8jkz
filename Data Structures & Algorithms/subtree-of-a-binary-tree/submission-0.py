# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isDuplicate(node, subNode):
            if (node and not subNode) or (subNode and not node):
                return False
            elif node and subNode and node.val == subNode.val:
                return isDuplicate(node.left, subNode.left) and isDuplicate(node.right, subNode.right)
            else:
                return True
        
        def dfs_root(node):
            if node is None:
                return False

            if node.val == subRoot.val:
                res = isDuplicate(node, subRoot)
                #print(res)
                return res

            return dfs_root(node.left) or dfs_root(node.right)

        return dfs_root(root)


    