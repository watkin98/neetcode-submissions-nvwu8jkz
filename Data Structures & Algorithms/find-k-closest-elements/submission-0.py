class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_diff = [arr[-1], 0]

        for i in range(len(arr)):
            diff = abs(x - arr[i])

            if diff >= closest_diff[0]:
                break
            closest_diff = [diff, i]
            
        res = [arr[closest_diff[1]]]
        starting_i = closest_diff[1]

        left = starting_i - 1 if starting_i - 1 >= 0 else None
        right = starting_i + 1 if starting_i + 1 < len(arr) else None
        while len(res) < k:
            if left == None:
                closest = arr[right]
            elif right == None:
                closest = arr[left]
            else:
                closest = min(arr[left], arr[right])

            if left != None and closest == arr[left]:
                res.insert(0, closest)
                left = left - 1 if left - 1 >= 0 else None
            else:
                res.append(closest)
                right = right + 1 if right + 1 < len(arr) else None

        return res

        