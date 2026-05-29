class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            print(f"m: {m}")
            if target > nums[m]:
                l = m + 1
                print(1)
            elif target < nums[m]:
                r = m - 1
                print(2)
            else:
                return m

        return -1