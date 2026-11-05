class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(l, r):
            if l > r:
                return None
            m = (l+r) // 2

            return TreeNode(nums[m], build(0, m-1), build(m+1, len(nums)-1))
        
        return build(0, len(nums) - 1)
            
