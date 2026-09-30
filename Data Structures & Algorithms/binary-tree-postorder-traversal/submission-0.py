# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorderSearch(node) -> None:
            if node is None:
                return

            postorderSearch(node.left)
            postorderSearch(node.right)
            res.append(node.val)

        postorderSearch(root)
        return res