class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        numSet = set(arr)

        for num in arr:
            if num + 1 in numSet:
                res += 1

        return res