class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start_i = self.findClosestNum(arr, x)
        return self.findClosestK(arr, k, x, start_i)
        
    def findClosestNum(self, arr, x) -> int:
        l, r = 0, len(arr) - 1
        i = 0

        while l <= r:
            m = l + ((r-l) // 2)
            if arr[m] == x:
                return m

            diff = abs(arr[m] - x)

            if diff <= abs(arr[i] - x):
                i = m
                l = m + 1
            elif diff > abs(arr[i] - x):
                r = m - 1
        return i

    def findClosestK(self, arr, k, x, i) -> List[int]:
        r = l = i
    
        while (r-l < k):
            
            l = l - 1 #if l - 1 >= 0 else l
            r = r + 1 #if r + 1 < len(arr) else r

            if l < 0:
                l = 0
            elif r > len(arr) - 1:
                r = len(arr) - 1
            else:
                left = arr[l]
                right = arr[r]

                if abs(left - x) <= abs(right - x):
                    r -= 1
                else:
                    l += 1

        return arr[l:r]




