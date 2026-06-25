class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mapping = defaultdict(int)

        for num in nums:
            if mapping[num] == 0:
                mapping[num] += 1
            elif mapping[num] == 1:
                mapping[num] -= 1

        for key in mapping:
            if mapping[key] == 1:
                return False

        return True