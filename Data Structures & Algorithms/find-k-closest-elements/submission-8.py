class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        candidate = [float('inf'), 0] # [difference, index]
        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + ((r-l) // 2)
            diff = abs(x - arr[m])
            if diff < candidate[0]:
                candidate = [diff, m]

            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                candidate = [0, m]
                break

        start_i = candidate[1]

        l = r = start_i

        while r - l + 1 < k:
            left = right = None
            if l-1 >= 0:
                left = arr[l-1]

            if r+1 < len(arr):
                right = arr[r+1]

            if left == None:
                r += 1
            elif right == None:
                l -= 1
            else:
                if abs(x-left) <= abs(x-right):
                    l -= 1
                else:
                    r += 1

        return arr[l:r+1]






            