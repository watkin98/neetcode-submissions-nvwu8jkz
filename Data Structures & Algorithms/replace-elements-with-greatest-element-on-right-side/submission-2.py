class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestElement = arr[len(arr) - 1]
        arr[-1] = -1
        
        for i in range(len(arr) - 2, -1, -1):
            tempElement = arr[i]
            arr[i] = greatestElement
            greatestElement = max(greatestElement, tempElement)

        return arr