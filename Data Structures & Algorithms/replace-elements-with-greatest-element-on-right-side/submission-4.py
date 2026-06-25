class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        maxNum = arr[n]
        arr[n] = -1

        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxNum
            maxNum = max(maxNum, temp)

        return arr