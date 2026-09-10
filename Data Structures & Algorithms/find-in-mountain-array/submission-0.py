class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1
        peak = None
        res = None

        while l <= r:
            m = l + ((r-l) // 2)
            spot = mountainArr.get(m)
            left = mountainArr.get(m-1)
            right = mountainArr.get(m+1)

            if left < spot < right:
                l = m + 1
            elif left > spot > right:
                r = m - 1
            else: # left < spot > right
                peak = m
                res = spot
                break

        if res == target:
            return peak

        leftRes = self.searchLeft(peak, target, mountainArr)
        return leftRes if leftRes != -1 else self.searchRight(peak, target, mountainArr)
        # if leftRes == -1:
        #     return self.searchRight(peak, mountainArr)
        
        # return leftRes

    def searchLeft(self, peak, target, mountainArr) -> int:
        l, r = 0, peak - 1

        while l <= r:
            m = l + ((r-l) // 2)
            spot = mountainArr.get(m)

            if target > spot:
                l = m + 1
            elif target < spot:
                r = m - 1
            else:
                return m

        return -1
        
    def searchRight(self, peak, target, mountainArr) -> int:
        l, r = peak + 1, mountainArr.length() - 1
        
        while l <= r:
            m = l + ((r-l) // 2)
            spot = mountainArr.get(m)

            if target > spot:
                r = m - 1
            elif target < spot:
                l = m + 1
            else:
                return m

        return -1
