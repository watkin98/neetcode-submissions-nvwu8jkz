class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxVal = float('-inf')
        for i in range(k):
            maxVal = max(maxVal, nums[i])
        res.append(maxVal)
        l, r = 1, k

        while r < len(nums):
            res.append(max(nums[l:r+1]))
            l += 1
            r += 1

        return res