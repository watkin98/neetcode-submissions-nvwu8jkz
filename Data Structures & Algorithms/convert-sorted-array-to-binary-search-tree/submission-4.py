class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def builder(l, r) -> 'TreeNode':
            if l > r:
                return None

            m = (l+r) // 2

            return TreeNode(nums[m], builder(l, m-1), builder(m+1, r))

        return builder(0, len(nums) - 1)
