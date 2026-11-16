# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive function contract: returns the node that fits the conditions to be LCA. Base
    #                              case is when the nodes p & q are to the left and right 
    #                              (or vice versa) of the current node in the BST
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)