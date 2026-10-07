# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        prev = None

        while node != None:
            prev = node
            if val < node.val:
                node = node.left
            else:   # val > node
                node = node.right

        if prev == None:
            return TreeNode(val)
        
        node = TreeNode(val)
        if prev.val > val:
            prev.left = node
        else:
            prev.right = node

        return root

        