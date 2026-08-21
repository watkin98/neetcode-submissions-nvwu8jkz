class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_diff = [float('inf'), 0]

        for i in range(len(arr)):
            diff = abs(x - arr[i])

            if diff < closest_diff[0]:
                closest_diff = [diff, i]
            elif diff == closest_diff[0]:
                pass
            else:
                if arr[i] > x:
                    break
            
        res = [arr[closest_diff[1]]]
        starting_i = closest_diff[1]
        print(f"closest num {res[0]} at {starting_i}")

        left = starting_i - 1 if starting_i - 1 >= 0 else None
        right = starting_i + 1 if starting_i + 1 < len(arr) else None
        while len(res) < k:
            closest = None
            if left == None:
                closest = arr[right]
            elif right == None:
                closest = arr[left]
            else:
                diff_l = abs(x - arr[left])
                diff_r = abs(x - arr[right])

                candidate = min(diff_l, diff_r) if diff_l != diff_r else diff_l
                closest = arr[left] if candidate == diff_l else arr[right]
                
            if left != None and closest == arr[left]:
                res.insert(0, closest)
                left = left - 1 if left - 1 >= 0 else None
            else:
                res.append(closest)
                right = right + 1 if right + 1 < len(arr) else None

        return res

        