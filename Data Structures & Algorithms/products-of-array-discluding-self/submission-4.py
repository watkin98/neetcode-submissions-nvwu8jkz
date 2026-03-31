class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        post = [0] * n
        answ = [0] * n

        pref[0] = post[n - 1] = 1

        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        for i in range(n):
            answ[i] = pref[i] * post[i]

        return answ