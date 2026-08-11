class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        hasNotChanged = False
        while hasNotChanged is False:
            hasNotChanged = True
            for i in range(1, len(arr) - 1):
                for j in range(1, i+1):
                    if arr[j] < arr[j-1] and arr[j] < arr[j+1]:
                        arr[j] += 1
                        hasNotChanged = False
                    elif arr[j] > arr[j-1] and arr[j] > arr[j+1]:
                        arr[j] -= 1
                        hasNotChanged = False
                    else:
                        continue

        return arr