# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            level = []

            while qLen:
                curr = q.popleft()

                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                qLen -= 1

            if level:
                res.append(level)

        return res