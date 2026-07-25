class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float('inf')
        L = R = 0
        curSum = 0

        while R < len(nums):
            curSum += nums[R]

            while curSum >= target and L <= R:
                print(f"L, R: {L}, {R}\nminSize: {minSize}")
                minSize = min(minSize, R-L+1)
                curSum -= nums[L]
                L += 1
            R += 1

        if minSize == float('inf'):
            return 0
        else:
            return minSize