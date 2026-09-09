class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            candidate = l + ((r-l) // 2)

            subarrays = total = 0
            maxSum = 0
            for num in nums:
                total += num
                
                if total > candidate:
                    maxSum = max(maxSum, total)
                    total = num
                    subarrays += 1

            subarrays += 1
            #print(f"Sum candidate ({candidate}) resulted in {subarrays} subarrays")
            if subarrays <= k:
                res = min(res, candidate)
                r = candidate - 1
            else:   # subarrays > k:
                l = candidate + 1
            # else:
            #     res = min(res, candidate)
            #     r = candidate - 1

        return res