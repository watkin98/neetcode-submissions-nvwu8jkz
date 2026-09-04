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
        for r in range(k, len(nums)):
            window[nums[l]] -= 1
            window[nums[r]] = 1 + window.get(nums[r], 0)
            l += 1

            if res[-1] > nums[r]:
                res.append(res[-1])
                continue
            elif res[-1] == nums[r]:
                res.append(nums[r])
                continue
            else:
                res.append(nums[r])

        return res
            


