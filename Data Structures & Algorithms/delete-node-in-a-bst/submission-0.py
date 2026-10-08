# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        curr, prev = root, None

        while curr and curr.val != key:
            prev = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right

        if not curr: 
            return root
        print(1)
        if not curr.left and not curr.right:
            print(2)
            if prev.left.val == key:
                prev.left = None
            elif prev.right.val == key:
                prev.right = None
        elif curr.left and not curr.right:
            print(3)
            if prev.left.val == key:
                prev.left = curr.left
            elif prev.right.val == key:
                pre.right = curr.left
        elif not curr.left and curr.right:
            print(4)
            if prev.left.val == key:
                prev.left = curr.right
            elif prev.right.val == key:
                pre.right = curr.right
        else: # curr.left and curr.right:
            print(5)
            if prev.left.val == key:
                temp = curr.left
                prev.left = curr.right
                prev.left.left = temp
            elif prev.right.val == key:
                temp = curr.right
                prev.right = curr.right
                prev.right.right = temp
            

        print(6)
        return root





