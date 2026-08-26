class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxVal = float('-inf')
        window = {}

        for i in range(k):
            maxVal = max(maxVal, nums[i])
            window[nums[i]] = 1 + window.get(nums[i], 0)
        res.append(maxVal)

        l = 0
        maxWindowVal = maxVal
        for r in range(k, len(nums)):
            window[nums[l]] -= 1
            window[nums[r]] = 1 + window.get(nums[r], 0)
            if nums[l] == maxWindowVal and window[nums[l]] == 0:
                del window[nums[l]]
                maxWindowVal = float("-inf")
                for num in window:
                    maxWindowVal = max(maxWindowVal, num) if window[num] > 0 else maxWindowVal
            if nums[r] > maxWindowVal:
                maxWindowVal = nums[r]
            l += 1

            res.append(maxWindowVal)

        return res
            


