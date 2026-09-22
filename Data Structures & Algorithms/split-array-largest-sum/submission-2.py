class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        largestSum = r

        while l <= r:
            candidate = l + ((r-l) // 2)

            subarrays = curSum = 0
            for num in nums:
                curSum += num

                if curSum > candidate:
                    curSum = num
                    subarrays += 1
            subarrays += 1

            if subarrays <= k:
                largestSum = candidate
                r = candidate - 1
            else:
                l = candidate + 1
                
        return largestSum