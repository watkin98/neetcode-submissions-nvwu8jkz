class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            max_sum = l + ((r-l) // 2)

            subarray_sum = subarrays = 0
            for n in nums:
                subarray_sum += n

                if subarray_sum > max_sum:
                    subarray_sum = n
                    subarrays += 1
            subarrays += 1

            if subarrays > k:
                l = max_sum + 1
            else:
                res = max_sum
                r = max_sum - 1

        return res