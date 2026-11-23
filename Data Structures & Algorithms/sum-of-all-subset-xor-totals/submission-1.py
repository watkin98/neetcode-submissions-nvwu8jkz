class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []

        def explore(i):
            nonlocal res
            if i == len(nums):
                total = 0
                for num in subset:
                    total ^= num
                res += total
                return

            subset.append(nums[i])
            explore(i+1)

            subset.pop()
            explore(i+1)
            
        explore(0)
        return res