# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node_and_parent = self.search(root, None, key)
        if not node_and_parent:
            return root

        node, parent = node_and_parent
        if parent != None:
            self.delete(node_and_parent[0], node_and_parent[1])
        else:
            if not node.left and not node.right:
                root = None
            elif node.left and not node.right:
                root = node.left
            elif node.right and not node.left:
                root = node.right
            else:
                curr, prev = node.right, node
                while curr.left:
                    prev = curr
                    curr = curr.left
                node.val = curr.val
                self.delete(curr, prev)

        return root
        
    def search(self, node, parent, key):
        if not node:
            return None

        if node.val == key:
            return [node, parent]

        return self.search(node.left, node, key) or self.search(node.right, node, key)

    def delete(self, node, parent):
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return
        
        if node.left and not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        elif not node.left and node.right:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            curr, prev = node.right, node
            while curr.left:
                prev = curr
                curr = curr.left
            node.val = curr.val
            self.delete(curr, prev)
