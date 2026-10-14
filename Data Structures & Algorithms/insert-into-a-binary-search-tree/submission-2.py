# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(node):
            if (val < node.val and not node.left) or (val > node.val and not node.right):
                return node

            if val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        new_node = TreeNode(val)
        leaf_node = dfs(root)
        if val < leaf_node.val:
            leaf_node.left = new_node
        else:
            leaf_node.right = new_node

        return root