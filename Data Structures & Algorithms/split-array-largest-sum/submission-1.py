class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = l + ((r-l) // 2)

            total = count = 0
            for num in nums:
                total += num

                if total > m:
                    total = num
                    count += 1
            count += 1

            if count <= k:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res