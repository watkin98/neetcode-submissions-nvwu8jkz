class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res = 0

        for num in nums:

            if num != res:
                if count == 0:
                    res = num
                else:
                    count -= 1
            else:
                count += 1

        return res