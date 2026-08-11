class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        for i in range(1, len(arr) - 1):
            print(0)
            for j in range(1, i+1):
                print(1)
                if arr[j] < arr[j-1] and arr[j] < arr[j+1]:
                    arr[j] += 1
                elif arr[j] > arr[j-1] and arr[j] > arr[j+1]:
                    arr[j] -= 1
                else:
                    continue

        return arr