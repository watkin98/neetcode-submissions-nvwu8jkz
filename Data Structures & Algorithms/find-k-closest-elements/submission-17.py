class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        start = l
        while l < r:
            m = l + ((r-l) // 2)

            if abs(arr[start] - x) >= abs(arr[m] - x):
                start = m
                l = m + 1
            else:   # abs(arr[start] - x) < abs(arr[m] - x):
                r = m - 1
        
        l, r = start - 1, start

        while (r-l+1) < k:
            print(f"l, r: {l}, {r}")
            if l < 0:
                r += 1
            elif r > len(arr) - 1:
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
            print(f"new l, r: {l}, {r}")
            print(f"r-l+1: {r-l+1}")

        return arr[l:r + 1] if l >= 0 else arr[l+1:r+2]