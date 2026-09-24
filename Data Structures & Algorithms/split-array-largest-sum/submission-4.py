class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            testSum = l + ((r-l) // 2)
            
            curSum, total = 0, k
            for n in nums:
                curSum += n

                if curSum > testSum:
                    curSum = n
                    total -= 1
            total -= 1

            if total < 0:
                l = testSum + 1
            else:
                res = testSum
                r = testSum - 1
        return res