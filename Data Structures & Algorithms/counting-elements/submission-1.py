class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        count = set(arr)

        for i in range(len(arr)):
            if arr[i] + 1 in count:
                res += 1

        return res

        