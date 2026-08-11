class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True

        while changed is True:
            changed = False

            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    arr[i] += 1
                    changed = True
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    arr[i] -= 1
                    changed = True
                else:
                    continue

        return arr