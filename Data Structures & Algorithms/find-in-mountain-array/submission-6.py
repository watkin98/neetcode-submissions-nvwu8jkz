class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        def findPeak() -> int:
            l, r = 0, mountainArr.length() - 1

            while l <= r:
                m = l + ((r-l) // 2)

                spot = mountainArr.get(m)
                left = mountainArr.get(m-1)
                right = mountainArr.get(m+1)

                if left < spot < right:
                    l = m + 1
                elif right < spot < left:
                    r = m - 1
                else: # left < spot > right:
                    return m
        
        def left(peak) -> int:
            l, r = 0, peak

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

        def right(peak) -> int:
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

        peak = findPeak()
        left = left(peak)
        return left if left != -1 else right(peak)