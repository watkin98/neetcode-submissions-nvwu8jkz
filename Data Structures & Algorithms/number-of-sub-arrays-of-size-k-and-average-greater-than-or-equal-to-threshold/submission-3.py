class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        window = k
        L, R = 0, window

        while R <= len(arr):
            windowSum = 0
            for i in range(L, R):
                windowSum += arr[i]
            avg = windowSum / window

            if avg >= threshold:
                res += 1
            
            L += 1
            R += 1

        return res
            