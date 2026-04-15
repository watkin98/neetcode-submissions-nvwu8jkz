class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rgt = [0] * n
        lft = [0] * n
        res = [0] * n

        lft[0] = rgt[n-1] = 1
        for i in range(1, n):
            lft[i] = lft[i-1] * nums[i-1]

        print(f"lft: {lft}")
        for i in range(n-2, -1, -1):
            rgt[i] = rgt[i+1] * nums[i+1]
        
        print(f"rgt: {rgt}")

        for i in range(n):
            res[i] = lft[i] * rgt[i]

        return res