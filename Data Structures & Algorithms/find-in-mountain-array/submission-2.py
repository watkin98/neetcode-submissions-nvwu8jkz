class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak = self.findPeak(mountainArr)
        if mountainArr.get(peak) == target:
            return peak

        leftSearch = self.searchLeft(target, mountainArr, peak)

        return leftSearch if leftSearch != -1 else self.searchRight(target, mountainArr, peak)

    def findPeak(self, mountainArr) -> int:
        l, r = 0, mountainArr.length() - 1

        while l <= r:
            m = l + ((r-l) // 2)
            spot = mountainArr.get(m)
            left = mountainArr.get(m - 1)
            right = mountainArr.get(m + 1)

            if left < spot < right:
                l = m + 1
            elif left > spot > right:
                r = m - 1
            else:
                return m

    def searchLeft(self, target, mountainArr, peak) -> int:
        l, r = 0, peak - 1

        while l <= r:
            m = l + ((r-l) // 2)
            spot = mountainArr.get(m)

            if target < spot:
                r = m - 1
            elif target > spot:
                l = m + 1
            else:
                return m

        return -1

    def searchRight(self, target, mountainArr, peak) -> int:
        l, r = peak + 1, mountainArr.length() - 1

        while l <= r:
            m = l + ((r-l) // 2)
            spot = mountainArr.get(m)

            if target < spot:
                l = m + 1
            elif target > spot:
                r = m - 1
            else:
                return m

        return -1