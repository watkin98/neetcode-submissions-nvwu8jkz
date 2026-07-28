class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        
        res = 1
        i = 0

        while i < len(arr) - 1 and arr[i] == arr[i+1]:
            i += 1

        if i == len(arr) - 1:
            return res
        
        increasing = False
        curMax = 1
        if arr[i+1] > arr[i]:
            increasing = True

        curMax += 1
        res = curMax
        i += 1

        for i in range(i, len(arr) - 1):
            if increasing and arr[i+1] < arr[i]:
                increasing = False
                curMax += 1
            elif not increasing and arr[i+1] > arr[i]:
                increasing = True
                curMax += 1
            else:
                if arr[i+1] == arr[i]:
                    curMax = 1
                else:
                    curMax = 2
                    increasing = arr[i+1] > arr[i]
            res = max(res, curMax)

        return res