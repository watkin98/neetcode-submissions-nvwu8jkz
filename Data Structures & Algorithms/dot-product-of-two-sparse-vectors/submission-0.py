class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        n = len(self.nums)
        i = 0
        res = 0

        while i < n:
            if self.nums[i] == 0 or vec.nums[i] == 0:
                i += 1
                continue

            res += self.nums[i] * vec.nums[i]
            i += 1

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
